<template>
    <div id="navbar">
            <h1 style="margin:10px;color:#ff5d9e; font-size: 400%;">MUSICK</h1>
            <div @click="emitPls('Home')"><i class="fa fa-home"></i> <span>Your Music</span></div>
            <div @click="emitPls('Playlist')"><i class="fa fa-music"></i> <span>Your Playlist</span></div>
            <div @click="emitPls('Artist')"><i class="fa fa-user"></i> <span>Your Artists</span></div>
            <div @click="emitPls('Download')">Download</div>
    </div>
        
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:"navbar",
    methods:{
        emitPls(comp){
            EventBus.$emit(comp)
        }
    }
}
</script>

<style>
#navbar{
    display: flex;
    width:20%;
    
    position: fixed;
    height:100%;
    background-color: #212121;
    flex-direction: column;
}
#navbar div{
    line-height: 2em;
    margin:10px;
    
}
#navbar div:hover{
    cursor: pointer;
    font-size: 110%;
}
.fa{
    
    padding:5px;
    font-size:1.5em;
}
span{
    width:70%;
}
</style>
