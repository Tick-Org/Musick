
<template>

    <input id="search-p" placeholder="Searches go here"  @change="pull" @input="$emit('input', $event.target.value)" @focus="change" />
    
</template>
<script>
import { EventBus } from "../event-bus.js";

export default {
    name:"searchComp",
    data(){
        return{
            message:""
        }
    },
    methods:{
        change(){
            EventBus.$emit("search-f")
        },
        pull(){
            console.log("pullUP")
            document.getElementById("search-p").style.top="-25%"
            EventBus.$emit("search-o")
        }
    }

}
</script>
<style>
#search-p{
    position: absolute;
    top:-25%;
    border: none;
    font-size:5em;
    height:25%;
    z-index:99;
    background-color:#233142;
    width: 80%;
    padding:5px;
    transition: all .2s ease-in-out;
}
</style>
