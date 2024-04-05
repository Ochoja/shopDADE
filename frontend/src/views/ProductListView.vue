<script setup>
import { ref } from 'vue'

const title = ref('') // page title

const params = $route.query

console.log(params)
</script>

<template>
  <div class="main">
    <h1>{{ title }} Products</h1>

    <div class="products"></div>
  </div>
</template>

<style lang="scss" scoped>
.main {
  @include grid-width;

  .products {
    @include product-grid;
    margin-bottom: 30px auto;
  }
}
</style>
