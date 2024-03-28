<script setup>
import { RouterView } from 'vue-router'
import Footer from './components/TheFooter.vue'
import Navigation from './components/TheNavigation.vue'
</script>

<template>
  <Navigation></Navigation>
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
