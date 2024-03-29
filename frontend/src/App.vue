<script setup>
import { computed } from 'vue'
import { RouterView, useRoute } from 'vue-router'
import Footer from './components/TheFooter.vue'
import Navigation from './components/TheNavigation.vue'

const route = useRoute()

// hide navigation in auth page
const showNav = computed(() => {
  if (route.path.includes('/auth/')) {
    return false
  } else {
    return true
  }
})
</script>

<template>
  <Navigation v-if="showNav"></Navigation>
  <RouterView />
  <Footer></Footer>
</template>

<style lang="scss">
.logo {
  font-family: 'Rammetto One';
  font-size: 1.5em;

  a {
    text-decoration: none;
  }
}
</style>
