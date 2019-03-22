<template>
    <div id ="search" @click="pull"><i class="fa fa-search-plus"></i></div>
</template>

<script>
import { EventBus } from "../event-bus.js";
export default {
    name:"search",
    methods:{
        pull(){
            console.log("pull")
            document.getElementById("search-p").style.top="0"
        }
    },
}
</script>

<style>

#search{
    position: fixed;
    top:0;
    font-size: 5em;
    color: #f3f9fb;
    
    right: 5px;
}

</style>
