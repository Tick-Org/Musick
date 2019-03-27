<template>
<div id="download">
    
    <input placeholder="Paste Spotify Link here" v-model="link" type="text" id="down"/>
    <button @click="download">Download</button>
</div>    
</template>

<script>
export default {
    data(){
        return{link:""}
        
    },
    methods:{
        download(){
            
            $.getJSON('http://127.0.0.1:5000/download/'+window.btoa(this.link).replace("/","***"), function(data) {
                console.log(data)
            });
        }
    }
}
</script>

<style>
#download{
    margin:10px;
}
#down{
    width:80%;
    background: none;
    padding:10px;
    border-radius: 40px;
    border:solid 1px;
}
button{
    
    background:#212121;
    border:none;
    padding:5px;
    margin:5px;
    border-radius: 4%;
}
</style>
