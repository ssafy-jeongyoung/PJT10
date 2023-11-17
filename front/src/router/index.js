import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import Depositview from '@/views/Depositview.vue'
import Exchangeview from '@/views/Exchangeview.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView
    },

    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },

    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },

    {
      path: '/deposit',
      name: 'deposit',
      component: Depositview
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: Exchangeview
    },
  ]
})

export default router
