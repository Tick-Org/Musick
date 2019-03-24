<template>
    <div  id="parent">
        <navbar></navbar>
        
        <div id="parent-r">
            <searchComp v-model="SQuery"></searchComp>
            <div id="music-head"><h2 style="margin:5% 0 5% 5%  ;font-size: 3em;" v-show="home">Home</h2></div>
            <search v-show="searchCom"></search>

            <song :SQuery="SQuery"></song>
            <player ></player>    
        </div>
        
    </div>
</template>

<script>
import navbar from "./navbar";
import player from "./player"
import search from "./search"
import song from "./home"
import { EventBus } from "../event-bus.js";
import searchComp  from "./searchSongComponent";
export default {
    name:'musicContainer',
    components: {navbar,player,search,song,searchComp},
    data(){
        return{
            searchCom:true,
            SQuery:"",
            home:true,
            playlist:false,
            artist:false,
            genres:false,
            albums:false
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
            this.home= true
            this.playlist = false
            this.artist = false
            this.album = false
            this.genres = false
        });
        EventBus.$on("Playlist",()=>{
            this.home= false
            this.playlist = true
            this.artist = false
            this.album = false
            this.genres = false
        });
        EventBus.$on("Artist",()=>{
            this.home= false
            this.playlist = false
            this.artist = true
            this.album = false
            this.genres = false
        });
        EventBus.$on("Genre",()=>{
            console.log("Genre")
            this.home= false
            this.playlist = false
            this.artist = false
            this.album = false
            this.genres = true
        });
    }
    
    
}
</script>

<style>

</style>
