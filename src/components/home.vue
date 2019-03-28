
<template>
    <div id="songs">
        
        <template   v-for="song,index in songs">
            
            <template v-if="song.title.toLowerCase().includes(SQuery.toLowerCase())||song.artist.toLowerCase().includes(SQuery.toLowerCase())">
                <div id="song">
                    <div style="position:relative" @click="playmusic(index,song.path,song.title,song.artist,pictures[index])">
                       
                        <img id="art" :src="pictures[index]"/>
                        <p id="songName"  >{{song.title}}</p>
                        <p id="artistName">{{song.artist}}</p>
                    </div>  
                </div>
            </template>
        </template>
    </div>
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:'song',
    props:["SQuery"],
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
        
        return{songs:allSongs,pictures:pictures}
    },
    
    methods:{
        playmusic(index,path,title,artist,art){
            
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
}
</style>
