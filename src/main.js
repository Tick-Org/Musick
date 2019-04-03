import Vue from 'vue'
import musicContainer from "./components/parentContainer"
import vmodal from 'vue-js-modal'
Vue.use(vmodal, { dialog: true,dynamic: true, injectModalsContainer: true  })
new Vue({
  el:  "#parent",
  render: cont => cont(musicContainer),
  
})