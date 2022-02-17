import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '../views/Layout.vue'
import TestCase from '../views/Testcase.vue'
import Task from '../views/Task.vue'

Vue.use(VueRouter)

// 路由管理
const routes = [
  {
    // 指定路由
    path: '/',
    // 组件
    // component: Home,
    // 指定重定向页面
    redirect:"/layout"
  },
  {
      path: '/layout',
      component: Layout,
      children:[
          {
              path:'testcase',
              name:'testcase',
              component:TestCase
          },
          {
              path:'task',
              name:'task',
              component:Task
          }
      ]
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
