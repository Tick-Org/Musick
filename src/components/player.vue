<template>
    <div id="player">
        
             <range-slider
             @change="changePlayHead"
    class="slider"
    min="0"
    max="100"
    step="0.1"
    v-model="sliderValue">
  </range-slider>
        
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

import RangeSlider from 'vue-range-slider'

export default {
    name:"player",
    
  components: {
    RangeSlider
  },
    data(){
        return {
            songName:""   ,
            artist:"",
            play:false,
            audio:new Audio(),
            sliderValue: 0,
            art:"",
            playing:false,
            sliderValue:0
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
            this.sliderValue=0
            this.audio = new Audio("http://127.0.0.1:5000/play/"+window.btoa(stuff[2]));
            
            this.playFunc()
        });
  },
  methods:{
        changePlayHead(value){
            this.pause()
            this.audio.currentTime = (value*this.audio.duration)/100
            console.log(value*this.audio.duration)
            this.playFunc()
        },
        playFunc(){
            this.playing = true
            this.audio.play()
            this.play=true
            var vm = this
            function set(percentage){if(vm.playing){vm.sliderValue+=percentage}}
            this.audio.addEventListener("loadeddata", function() {
                var percentage = 1/(this.duration*10)
                
                setInterval(()=>set(percentage),1)
            });
            
        },
        
        pause(){
            this.playing = false
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
    
    bottom:0px;
    position: fixed;
    padding-bottom: 1em;
    padding:0;
 
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
.slider{
    height:5%;
    width:65em;
    margin:0;
    
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



