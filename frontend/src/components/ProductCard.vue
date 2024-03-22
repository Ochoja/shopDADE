<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  product: Object
})
</script>

<template>
  <RouterLink to="/" class="product">
    <div class="img">
      <img :src="product.image" alt="Product_Image" />
    </div>
    <div class="name">{{ product.product_name }}</div>
    <div class="price">${{ product.price }}</div>
  </RouterLink>
</template>

<style lang="scss" scoped>
.product {
  text-decoration: none;
  text-align: left;
  color: #000;
  font-size: 1.1em;
  display: flex;
  flex-direction: column;

  .img {
    object-fit: cover;
    margin-bottom: 14px;

    img {
      border-radius: 10px;
      object-fit: contain;
      height: auto;
      width: inherit;
    }
  }

  .name {
    font-weight: 600;
    // font
  }
}
</style>
