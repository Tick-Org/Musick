<template>
    <div id="player">
        <div id="player-p"></div>
        <div id="content-play">
            <img id="alb" :src="art"/>
            <div id="name">
            <p id="songNameT">{{songName}}</p>
            
            <p style="font-size:70%">{{artist}}</p>
            </div>
            <div class="media" @click="playFunc" v-show="!play"><p><i class="fa fa-play-circle"></i></p></div>
            <div class="media" @click="pause" v-show="play"><p><i class="fa fa-pause-circle"></i></p></div>
            
        </div>
    </div>
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:"player",
    
    data(){
        return {
            songName:""   ,
            artist:"",
            play:false,
            audio:new Audio(),
            sliderValue: 0,
            art:"",
            
            
        }
    },
    created() {
        EventBus.$on("play", stuff => {
            this.songName = stuff[0]
            this.pause()
            this.artist = stuff[1]
            this.art = stuff[3]
            if(this.play){this.audio.pause()}
            this.play = true
            document.getElementById("player-p").style.width="0%"
            this.audio = new Audio("http://127.0.0.1:5000/play/"+window.btoa(stuff[2]));
            this.playFunc()
        });
  },
  methods:{
        playFunc(){
            this.audio.play()
            this.play=true
            
            //wait for it to load
            setTimeout(() => {
                $("#player-p").animate({width: "65em"},(this.audio.duration*1000));
                
            }, 500);
            
        },
        pause(){
            this.audio.pause()
            $("#player-p").stop()
            this.play=false;
        },
       
  }
}
</script>
<style>
#player{
    background-color: #212121;
    width: 100%;
    height: 10%;
    bottom:0px;
    position: fixed;
    padding-bottom: 1em;
    
}
#name{
    width:50em
}
#content-play{
    width: 100%;
    display: flex;
}
.media{
    font-size: 1.7em;
    margin-left:10%;
}
#player-p{
    height:5%;
    background-color: aliceblue;
}
#alb{
    height:3%;
    width:3%;
    margin:10px;
    padding:5px;
}
#songNameT{
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
}
</style>



