<template>
    <div id="navbar">
            <h1 style="margin:10px;color:#ff5d9e; font-size: 400%;">MUSICK</h1>
            <div @click="EventBox.$emit('Home')">Your Music</div>
            <div @click="EventBox.$emit('PlayList')">Your Playlist</div>
            <div @click="EventBox.$emit('Artist')">Your Artists</div>
            <div @click="EventBox.$emit('Genre')">Your Genres</div>
    </div>
        
</template>
<script>
import { EventBus } from "../event-bus.js";
export default {
    name:"navbar"
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
