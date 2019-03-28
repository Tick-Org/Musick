<template>
    <div id="player">
        
             <range-slider
             @change="changePlayHead"
    class="slider"
    min="0"
    max="100"
    step="0.001"
    v-model="sliderValue">
  </range-slider>
        
        <div id="content-play">
            <img id="alb" :src="art"/>
            <div id="name">
            <p id="songNameT">{{songName}}</p>
            
            <p style="font-size:80%">{{artist}}</p>
            </div>
            <div class="mediaa">
                <div class="mp"><i class="fa fa-backward"></i></div>
                
                <div class="media" @click="playFunc" v-show="!play"><i class="fa fa-play-circle"></i></div>
                <div class="media" @click="pause" v-show="play"><i class="fa fa-pause-circle"></i></div>

                <div class="mp"><i class="fa fa-forward"></i></div>
            </div>
            
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
            duration:0,
            art:"",
            playing:false,
            
            sliderValue:0
        }
    },
    created() {
        EventBus.$on("play", stuff => {
            
            this.songName = stuff[1]
            this.pause()
            this.artist = stuff[2]
            this.art = stuff[4]
            if(this.play){this.audio.pause()}
            this.play = true
            this.sliderValue=0
            this.audio = null
            var vm = this
            this.audio = new Audio("http://127.0.0.1:5000/play/"+window.btoa(stuff[3]));
            this.audio.addEventListener("loadeddata", function() {
                vm.duration = this.duration
            });
           
            

            
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
            this.audio.pause()
            this.play=true
            var vm = this
            var duration = 0
            this.audio.ontimeupdate=function(){
                vm.sliderValue = (vm.audio.currentTime / vm.audio.duration ) * 100
            }
            this.audio.play()
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
    background-color: rgb(33, 33, 33,0.8);
    width: 100%;
    
    bottom:0px;
    position: fixed;
    padding-bottom: 1em;
    padding:0;
 
}
.mediaa{
    font-size: 1.7em;
    display:flex;
}
.mediaa div{
    padding:5px;
}
#name{
    width:50em
}
#content-play{
    width: 100%;
    display: flex;
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



