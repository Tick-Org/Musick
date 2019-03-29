<template>
    <div  id="parent">
        <navbar></navbar>
        
        <div id="parent-r">
            <searchComp v-model="SQuery"></searchComp>
            <div id="music-head"><h2 style="margin:5% 0 5% 5%  ;font-size: 3em;">{{Screen}}</h2></div>
            <search v-show="searchCom && !download"></search>
            <div style="display:flex;margin:5px;"><div @click="typeChangeSquare" style="width:20px;" class="fa fa-th-large"></div><div @click="typeChangeList" color= "#dee0d9" class="fa fa-th-list"></div></div>
            <song :square="square" :SQuery="SQuery" v-show="!download"></song>
            <download v-show="download"></download>
            <player ></player>    
        </div>
        
    </div>
</template>

<script>
import navbar from "./navbar";
import player from "./player"
import download from "./download"
import search from "./search"
import song from "./home"
import { EventBus } from "../event-bus.js";
import searchComp  from "./searchSongComponent";
export default {
    name:'musicContainer',
    components: {navbar,player,search,song,searchComp,download},
    data(){
        return{
            searchCom:true,
            SQuery:"",
            Screen:"Home",
            home:true,
            playlist:false,
            artist:false,
            genres:false,
            albums:false,
            square:true,
            download:false,
        }
    },
    methods:{
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
            this.genres = false
            this.download = false
        });
        EventBus.$on("Playlist",()=>{
            this.Screen = "Playlist"
            this.home= false
            this.playlist = true
            this.artist = false
            this.album = false
            this.genres = false
            this.download = false
        });
        EventBus.$on("Artist",()=>{
            this.Screen = "Artist"
            this.home= false
            this.playlist = false
            this.artist = true
            this.download = false
            this.album = false
            this.genres = false
        });
        EventBus.$on("Download",()=>{
            this.Screen = "Download"
            this.home= false
            this.playlist = false
            this.artist = false
            this.album = false
            this.genres = false
            this.download = true
        });
    }
    
    
}
</script>

<style>

</style>
