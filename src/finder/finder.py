import base64
from flask import Flask
app = Flask(__name__)
import os
from flask import jsonify,send_file
import getpass
import eyed3

from flask_cors import CORS, cross_origin
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#http://127.0.0.1:5000/songList
#http://127.0.0.1:5000/play/
music_dir = list(filter(lambda x:x[-3:]=="mp3",os.listdir("/home/"+getpass.getuser()+"/Music")))
down_dir = list(filter(lambda x: x[-3:]=="mp3",os.listdir("/home/"+getpass.getuser()+"/Downloads")))
all_dir=music_dir+down_dir

@app.route("/songlist")
@cross_origin()
def songList():
    tags=[]
    for song in all_dir:
        dicts={}
        path = ""
        tag = object()
        try:
            path = "/home/"+getpass.getuser()+"/Music/"+song
            tag = eyed3.load(path)
        except OSError :
            path = path = "/home/"+getpass.getuser()+"/Downloads/"+song
            tag = eyed3.load(path)
        
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
    os.system("ffmpeg -i \""+listPath+"\" art/"+songName+".jpg -y")
    return send_file(os.getcwd()+"/art/"+songName+".jpg", mimetype='image/jpg')
@app.route("/play/<songName>")
@cross_origin()
def song(songName):

    try:
        listPath = base64.b64decode(songName).decode('utf-8')
    except:
        listPath = base64.b64decode(songName).decode('latin-1')
    return  send_file(listPath, mimetype='audio/mp3')
