import { createRouter, createWebHashHistory } from 'vue-router'
import HealthForm from '../views/HealthForm.vue'

const routes = [
  {
    path: '/',
    name: 'forms',
    component: HealthForm
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
