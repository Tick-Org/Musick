
<template>
    <div>
        <div style="display:flex;margin:5px;">
            <div @click="typeChangeSquare" style="width:20px;margin-right:20px;" class="fa fa-th-large"></div>
            <div @click="typeChangeList" color= "#dee0d9" class="fa fa-th-list"></div>
        </div>
        <div v-show="square" id="songs">
        
         <div  v-for="song,index in songs" :key="song.id"> 
            
            <template v-if="song.title.toLowerCase().includes(SQuery.toLowerCase())||song.artist.toLowerCase().includes(SQuery.toLowerCase())">
                <div id="song">
                    <div style="position:relative"  @click="playmusic(song.id,song.path,song.title,song.artist,pictures[index])">
                       <div class="ov" :id="song.id" v-show="playing"><div><i class="fa fa-music"></i></div></div>
                        <img id="art" :src="pictures[index]"/>
                        <p id="songName"  >{{song.title}}</p>
                        <p id="artistName">{{song.artist}}</p>
                    </div>  
                </div>
            </template>
        </div>
        </div>
        <div v-show="!square" id="line">
        
        <div   v-for="song,index in songs" :key="song.id">
            
            <template v-if="song.title.toLowerCase().includes(SQuery.toLowerCase())||song.artist.toLowerCase().includes(SQuery.toLowerCase())">
                <div  id="LineSong" >
                    <div style="display:flex;"  @click="playmusic(song.id,song.path,song.title,song.artist,pictures[index])">
                        <div :id="'line'+song.id" style="width:50%;" >{{song.title}}</div><div  style="font-size:80%;width:30%;">{{song.artist}}</div>
                        <div @click="playlist(song.path)" class='fa fa-plus-circle'></div>
                    </div>  
                </div>
            </template>
        </div>
        </div>
    <modals-container name="lists" id="dialog"/>
    </div>
    
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:'song',
    props:{SQuery:{type:String,default:""}},
    data(){
        
        var allSongs=[];
        var pictures=[]
        $.getJSON('http://127.0.0.1:5000/songlist', function(data) {
            
                data.forEach(element => {
                    try{    
                        const boa = window.btoa(element.path)
                        
                        allSongs.push(element)
                        pictures.push("http://127.0.0.1:5000/art/"+boa)
                    }
                    catch(err){
                        null
                    }
                });
        })
        var playlistL = []
        $.getJSON('http://127.0.0.1:5000/playlist/getPlaylist', function(data) {
                data.forEach(element => {
                    playlistL.push(element)
                });
        })
        
        
        return{songs:allSongs,playlistK:playlistL,pictures:pictures,playing:false,index:-1,square:true,status:{}}
    },
    created(){
       
        var vm = this
        EventBus.$on('back',function(params) {
                console.log(vm.index)
                var song = null
                console.log("length=>"+vm.songs.length)
            if(vm.index > 0){
   
                song = vm.songs[vm.index-1]
                vm.playmusic(vm.index-1,song.path,song.title,song.artist,vm.pictures[vm.index-1])
            }
            
        })
        EventBus.$on('forward',function(params) {
            var song = null
            if((vm.index < vm.songs.length)){
                song = vm.songs[vm.index+1]
                vm.playmusic(vm.index+1,song.path,song.title,song.artist,vm.pictures[vm.index+1])
            }
        })
    },
    methods:{
        playlist(title){
        var vm = this
        this.status["song"] = title
        this.$modal.show({
            title: 'Make A Playlist',
            template: `
            <div style="width:inherit;height:inherit;display:flex;flex-direction:column;text-align:center">
                <h1>Select a Playlist</h1>
                <p>Select a Playlist to add the Song</p>
                <div style="margin:10px;width:90%;height:50%;overflow-y:scroll">

                    <div   v-for="playlist in playlistsT">
                        <div  style="display:flex"><div style="width:fit-content"><input @click="select" type="checkbox" :value="playlist"></div><div style="width:100px;text-align:left">{{playlist}}</div><br/></div>
                    </div>
                
                </div>
                <button type="button" id="create" @click="add">Add to Playlist</button>   
            </div>
            `,
            props:["playlistsT","select","add"],
            
            },{playlistsT:vm.playlistK,select:this.select,add:this.add,},{width:"30%"})
            
        },
        select(event){
            
            this.status[event.target.value]=event.target.checked
            console.log(this.status)
        },
        add(event){

            this.$emit('close')
            for(var key in this.status){
                if(this.status[key]){
                    var playlist = key
                    if(key != "song"){
                        $.getJSON('http://127.0.0.1:5000/playlist/addSong/'+window.btoa(playlist)+"/"+window.btoa(this.status["song"]), function(data) {
                            console.log("done")
                        })
                    }
                }
            }
        },
        playmusic(index,path,title,artist,art){
            if(this.index != -1){
                this.playing=false
                if(document.getElementById(this.index) != null){
                    document.getElementById(this.index).style.zIndex = -1
                    document.getElementById("line"+this.index).style.color = "#eee"
                }
            }
            this.index = index
            this.playing=true
            try {
            document.getElementById(index).style.zIndex = 0
            document.getElementById("line"+this.index).style.color = "#00faac"
                
            } catch (error) {
                
            }
            EventBus.$emit("play",[index ,title,artist,path,art])
        },
        typeChangeSquare(event){
            console.log(event.target.style.color )
            event.target.style.color = "#f3f9fb"
            document.getElementsByClassName("fa-th-list").item(0).style.color =  "#dee0d9"
            
            this.square = true
        },

        typeChangeList(event){
            event.target.style.color = "#f3f9fb "
            
            document.getElementsByClassName("fa-th-large").item(0).style.color =  "#dee0d9"
            this.square = false
        }
    }
}
</script>
<style>
#songName{
    font-size:90%;
    width: inherit;
    height:20%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-weight: bold;
}
#artistName{
    font-size: 70%;
}
#create{
    border: none;
    padding:10px;
    background-color: #556fb5;
    color:#eee;
}
#songs{
    display: flex;
    flex-wrap: wrap;
    margin:15px;
    padding-bottom: 10%;
}
#LineSong{
    width:inherit;
    margin:10px;
    padding:15px;
    cursor: pointer;
    transition:  all .2s ease-in-out;
    border-bottom:solid 0.1px;
}
#LineSong:hover{
    transform:scale(1.01)
}
#line{
    padding-bottom: 10%;
}
.ov{

    width:12em;
    overflow: hidden;
    display: flex;
    justify-content: center;
    text-align: center;
    flex-direction: column;
    border-radius: 15px;
    height: 12em;
    opacity:0.8;
    position: absolute;
    z-index:-1;
    background-color: black;

}
#song{
    
    width:15em;
    
    height:18em;
    transition: all .2s ease-in-out;
    margin:5px;
}

#song:hover{
    transform: scale(1.05);
}
#art{
    width:80%;
    height: 70%;

    border-radius: 15px;
    transition:all .2s ease-in-out;
}
#art:hover{
    border-radius: 0px;
}
</style>
