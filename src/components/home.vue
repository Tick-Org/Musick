
<template>
    <div>
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
                        
                    </div>  
                </div>
            </template>
        </div>
        </div>
    </div>
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:'song',
    props:{SQuery:{type:String,default:""},square:{type:Boolean,default:true}},
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
        
        return{songs:allSongs,pictures:pictures,playing:false,index:-1}
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
            document.getElementById(index).style.zIndex = 0
            document.getElementById("line"+this.index).style.color = "#00faac"
            EventBus.$emit("play",[index ,title,artist,path,art])
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
