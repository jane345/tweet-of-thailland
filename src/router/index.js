import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import region from '@/components/region'
import detail from '@/components/detail'
import responsive from 'vue-responsive'
import addd from '@/components/AddFirebase'
import test from '@/components/test'
// import Ping from '@/components/ping'
// import Books from '@/components/book'
Vue.use(responsive)
Vue.use(Router)
/*
const Region = {
  template: `
    <div class="region">
      <router-view></router-view>
    </div>
  `
}
*/
export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
      // name: 'Books',
      // component: Books
    },
    {
      path: '/test',
      // name: 'home',
      // component: home
      name: 'test',
      component: test
    },
    {
      path: '/addja',
      name: 'add',
      component: addd
    },
    {
      path: '/:region',
      name: 'region',
      component: region
      /* children: [
        { path: 'ภาคเหนือ', component: north },
        { path: 'ภาคตะวันออกเฉียงเหนือ', component: northeast },
        { path: 'ภาคกลาง', component: central },
        { path: 'ภาคใต้', component: south },
        { path: 'ภาคตะวันออก', component: east },
        { path: 'ภาคตะวันตก', component: west }
      ] */
    },
    {
      path: '/:regionName/:landmark',
      name: 'detail',
      component: detail
    }
  ],
  mode: 'history'
})
