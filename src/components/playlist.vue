<template>
    <div id="playlists">
        <div id="new" @click="modalS"><div class="fa fa-plus"></div></div>
    <v-dialog/>
    </div>

</template>

<script>

import { EventBus } from "../event-bus.js";

export default {
    
    name:"playlist",
    data:()=>({
        modal:false
    }),
    methods:{
        modalS(){
            this.$modal.show('dialog', {
              title: 'Make A Playlist',
              text: `
              
                <div style="display:flex">
                  <div><p>Playlist Name:</p></div>
                  <div style="display:flex;justify-content:center;"><input id="playlistName" style="border:none;width:80%; border-bottom:black solid 0.5px;height:40px"/></div>
                </div>
                
              `,
              
              buttons: [
                {
                  title: 'Create',
                  default:true,
                  handler: () => { 
                      
                        var playListName = window.btoa(document.getElementById("playlistName").value);

                        this.$modal.hide("dialog")
                      }
                },
                
                {
                  title: 'Close'
                }
             ]
            })
        }
    }

}
</script>

<style>
#new{
    width:2em;
    display: flex;
    justify-content: center;
    text-align: center;
    padding:5em;
    margin:10px;
    
    height:2em;
    padding:none;
    background-color:rgba(0,0,0,0.8); 
}
 .v--modal{
     color: black !important;
 }
</style>
