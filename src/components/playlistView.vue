<template>
    <div id="Playlist">
        <i style="margin:10px;" @click="goback" class="fa fa-arrow-circle-left"></i>
         <div style="margin:50px;"><h1>{{PlaylistName}}</h1><p style="font-size:80%;font-weight:100">Playlist</p></div>
         
         <div v-for="song in songs">
            <div>
                {{song.title}}
            </div>
            
         </div>
    </div>
</template>

<script>
import { EventBus } from "../event-bus.js";
export default {
    props:["PlaylistName"],
    data:()=>({
        songs:[]
    }),
    created(){
        var vm = this
        $.getJSON("127.0.0.1:5000/playlist/getSongs/"+window.btoa(this.PlaylistName),function(data){
            vm.songs = []
            data.forEach(element => {
                vm.songs.push(element)    
            });
            

        })
    },
    methods:{
        goback(){
            
            EventBus.$emit('back')
        }
    }
}
</script>

<style>

</style>
