import Vue from 'vue'
import musicContainer from "./components/parentContainer"
new Vue({
  el:  "#parent",
  render: cont => cont(musicContainer),
  
})