// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCRF6AVRaVihGULdtQw_lAJwf_FGThLcq8',
    libraries: 'places,directions' // necessary for places input
  }
})
Vue.config.productionTip = false
// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
