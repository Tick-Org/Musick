<template>
    <div  id="parent">
        <navbar></navbar>
        
        <div id="parent-r">
            <searchComp v-model="SQuery"></searchComp>
            <div id="music-head"><h2 style="margin:5% 0 5% 5%  ;font-size: 3em;">{{Screen}}</h2></div>
            <search v-show="searchCom && !download"></search>
            <template v-if="home"><song :SQuery="SQuery"></song></template>
            <template v-if="playlist"><playlist></playlist></template>
            <template v-if="download"><download></download></template>
            <player ></player>    
        </div>
        
    </div>
</template>

<script>
import navbar from "./navbar";
import player from "./player"
import download from "./download"
import search from "./search"
import playlist from "./playlist"
import song from "./home"
import { EventBus } from "../event-bus.js";
import searchComp  from "./searchSongComponent";
export default {
    name:'musicContainer',
    components: {navbar,player,search,song,searchComp,download,playlist},
    data(){
        return{
            searchCom:true,
            SQuery:"",
            Screen:"Home",
            home:true,
            playlist:false,
            artist:false,
            albums:false,
            square:true,
            download:false,
        }
    },
    created(){

        EventBus.$on("search-f",()=>{
            this.searchCom= false
        });
        EventBus.$on("search-o",()=>{
            this.searchCom= true
        });
        EventBus.$on("Home",()=>{
            this.Screen = "Home"
            this.home= true
            this.SQuery=""
            this.playlist = false
            this.searchCom= true
            this.artist = false
            this.album = false
            this.download = false
        });
        EventBus.$on("Playlist",()=>{
            this.Screen = "Playlist"
            this.home= false
            this.playlist = true
            this.artist = false
            this.album = false
            this.download = false
        });
        EventBus.$on("Download",()=>{
            this.Screen = "Download"
            this.home= false
            this.playlist = false
            this.artist = false
            this.album = false
            
            this.download = true
        });
    }
    
    
}
</script>

<style>

</style>
