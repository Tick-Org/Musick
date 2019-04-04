<template>
    <div id="playlists">
      <Div id="squares" v-show="!playlistView">
        <div class="square" id="new" @click="modalS"><div class="fa fa-plus"></div></div>
        <div v-for="playlist in allPlaylist">
            <div class="square" id="new" @click="changeView(playlist)"><div>{{playlist}}</div></div>
        </div>
      </Div>        
      <template  v-if="playlistView">
          
          <play-list-view :PlaylistName="playlist"></play-list-view>
      </template>
    <v-dialog/>
    </div>

</template>

<script>

import { EventBus } from "../event-bus.js";
import PlayListView from "./playlistView.vue"
export default {
    
    name:"playlist",
    components:{PlayListView},
    data(){
      return{
            modal:false,
            allPlaylist:[],
            playlist:"",
            playlistView:false
        }
    },
    created(){
        EventBus.$on("back1",()=>{
          this.playlistView = false
        })
        this.getPlayLists()
    },
    methods:{
        changeView(name){
          this.playlist = name
          this.playlistView = true
        },
        getPlayLists(){
          var vm = this
          $.getJSON("http://127.0.0.1:5000/playlist/getPlaylist",function(data){

              vm.allPlaylist = []
              data.forEach(element => {
                
                vm.allPlaylist.push((element))
              });
          })
        },
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
                     $.getJSON('http://0.0.0.0:5000/playlist/create/'+playListName, function(data) {
                        console.log(data)
                    });
                    this.getPlayLists()
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
#squares{
  display: flex;
  flex-wrap: wrap; 
}
</style>
