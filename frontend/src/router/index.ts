import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/product/:id',
      name: 'product',
      component: () => import('../views/ProductView.vue'),
      props: true
    },
    {
      path: '/auth/:type',
      name: 'auth',
      component: () => import('../views/AuthView.vue'),
      props: true
    },
    {
      path: '/:user/cart',
      name: 'cart',
      component: () => import('../views/CartView.vue'),
      props: true
    }
  ]
})

export default router
