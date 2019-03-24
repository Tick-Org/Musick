<template>
    <div id="navbar">
            <h1 style="margin:10px;color:#ff5d9e; font-size: 400%;">MUSICK</h1>
            <div @click="emitPls('Home')">Your Music</div>
            <div @click="emitPls('Playlist')">Your Playlist</div>
            <div @click="emitPls('Artist')">Your Artists</div>
            <div @click="emitPls('Genre')">Your Genres</div>
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
    line-height: 3em;
}
#navbar div:hover{
    
    font-size: 110%;
}
</style>
