import base64
from flask import Flask
app = Flask(__name__)
import os
from flask import jsonify,send_file
import getpass
import eyed3
import subprocess as s

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/songlist")
@cross_origin()
def songList():

    music_dir = list(filter(lambda x:x[-3:]=="mp3",os.listdir("/home/"+getpass.getuser()+"/Music")))
    down_dir = list(filter(lambda x: x[-3:]=="mp3",os.listdir("/home/"+getpass.getuser()+"/Downloads")))
    all_dir=music_dir+down_dir
    
    tags=[]
    
    for idx,song in enumerate(all_dir):
        dicts={}
        path = ""
        tag = object()
        try:
            path = "/home/"+getpass.getuser()+"/Music/"+song
            tag = eyed3.load(path)
        except OSError :
            path = path = "/home/"+getpass.getuser()+"/Downloads/"+song
            tag = eyed3.load(path)
        dicts["id"] = idx 
        dicts["album"] = tag.tag.album
        dicts["title"] = tag.tag.title
        dicts["artist"] = tag.tag.artist
        dicts["path"] = path
        print(path)
        tags.append(dicts)
    return jsonify(tags)        
@app.route("/art/<songName>")
@cross_origin()
def art(songName):
    try:
        listPath = base64.b64decode(songName).decode('utf-8')
    except:
        listPath = base64.b64decode(songName).decode('latin-1')        
    try:
        os.mkdir(os.getcwd()+"/art")
    except FileExistsError:
        pass
    os.system("ffmpeg -i \""+listPath+"\" art/"+songName+".jpg -n")
    os.system("clear")
    try:
         open(os.getcwd()+"/art/"+songName+".jpg", 'r')
         return send_file(os.getcwd()+"/art/"+songName+".jpg", mimetype='image/jpg')
    except FileNotFoundError:
        return send_file(os.getcwd()+"/art/notfound.png", mimetype='image/png')
    
    
@app.route("/play/<songName>")
@cross_origin()
def song(songName):

    try:
        listPath = base64.b64decode(songName).decode('utf-8')
    except:
        listPath = base64.b64decode(songName).decode('latin-1')
    tag = eyed3.load(listPath)
    album= tag.tag.album
    title= tag.tag.title
    artist= tag.tag.artist
    
    notfound = " ".join(['notify-send',"\""+title+"\"","\""+artist+"\"","-i",os.getcwd()+"/art/notfound.png"])
    normal = " ".join(['notify-send',"\""+title+"\"","\""+artist+"\"","-i",os.getcwd()+"/art/"+songName+".jpg"])
    print(notfound)        
    try:
            open(os.getcwd()+"/art/"+songName+".jpg", 'r')
            print("doing")
            os.system(normal)
    except FileNotFoundError:
            print("doing")
            os.system(notfound)
    os.system("clear")
    return  send_file(listPath, mimetype='audio/mp3')

@app.route("/download/<songName>")
@cross_origin()
def download(songName):
    songLink =  base64.b64decode(songName.replace("***","/")).decode('utf-8')
    os.system("spotdl --song "+songLink)
    dicts={"status":"success"}
    
    return jsonify(dicts)
@app.route("/playlist/create/<playlistName>")
@cross_origin()
def playlist(playlistName):
    
    try:
        os.mkdir(os.getcwd()+"/playlist/")
    except FileExistsError:
        pass
    newPlayFile = open("playlist/"+playlistName+".txt","w+")   
    return jsonify({"success":"true"}) 
    
@app.route("/playlist/addSong/<playlistName>/<songName>") 
@cross_origin()
def getSongName(playlistName,songName):
    try:
        songNameRefined = base64.b64decode(songName).decode('utf-8')
    except:
        songNameRefined = base64.b64decode(songName).decode('latin-1')        
    playlist = open("playlist/"+playlistName+".txt","a+")               
    playlist.write(songNameRefined+"\n")
    return jsonify({"sucess":"true"})
@app.route("/playlist/getSongs/<playlistName>")  
@cross_origin()
def getSongsFromPlaylist(playlistName):
    
    songs =[]
    playlist = open("playlist/"+playlistName+".txt","r").read().split("\n")
    print(playlist)
    idx = 0
    for i in playlist:
        songTags = {}
        if i != "":
            print(i)
            idx+=1
            tag = eyed3.load(i)
            songTags["id"] = idx
            songTags["title"] = tag.tag.title
            songTags["artist"] = tag.tag.artist
            songTags["album"] = tag.tag.album
            songTags["path"] = i
            songs.append(songTags)

    return jsonify(songs)
@app.route("/playlist/getPlaylist")
@cross_origin()    
def getPlaylists():
    plays=[]
    for playlist in os.listdir(os.getcwd()+"/playlist/"):
        listPath =base64.b64decode(playlist.replace(".txt","")).decode('utf-8')

        print(listPath)            
        
        plays.append(listPath)            

    return jsonify(plays)
app.run(host='0.0.0.0',port="7000")