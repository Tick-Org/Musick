<template>
    <div id="Playlist" style="padding-bottom:10%;">
        <i style="margin:10px;" @click="goback" class="fa fa-arrow-circle-left"></i>
         <div style="margin:50px;"><h1>{{PlaylistName}}</h1><p style="font-size:80%;font-weight:100">Playlist</p></div>
         <hr style="width:90%;color:#eee;"/>
         <div style="margin:50px;" v-for="song,index in songs" :key="song.id">
            <div :id="'line'+song.id"  style="display:flex;flex:1"  @click="playmusic(song.id,song.path,song.title,song.artist,pictures[index])">
                
                <div style="width:60%;">{{song.title}}</div>
                <div style="width:40%;">{{song.artist}}</div>


            </div>
            
         </div>
    </div>
</template>

<script>
import { EventBus } from "../event-bus.js";
export default {
    props:["PlaylistName"],
    data(){
        return{songs:[],pictures:[]}
    },
    created(){

        var vm = this
        var url = "127.0.0.1:5000/playlist/getSongs/"+window.btoa(vm.PlaylistName)
        console.log(url)
        fetch("http://127.0.0.1:5000/playlist/getSongs/Q3JlYXRl")
        .then(res => res.json())
        .then((out) => {
          vm.songs = out

      vm.songs.forEach(element => {
        const boa = window.btoa(element.path)
        console.log(vm.pictures)
        vm.pictures.push("http://127.0.0.1:5000/art/"+boa)
      });
        })
    },
    methods:{
        goback(){
            
            EventBus.$emit('back1')
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
    }
}
</script>

<style>

</style>
