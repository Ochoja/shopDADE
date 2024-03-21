<script setup>
import { Icon } from '@iconify/vue'
</script>

<template>
  <footer>
    <div class="items">
      <div class="brand">
        <div class="logo">shopDADE</div>
        <p>
          Discover our latest arrivals, curated for the modern working class, shop now to elevate
          your wardrobe with fresh sophistication and style.
        </p>
      </div>
      <div class="links">
        <h3>Collections</h3>
        <div>Suit</div>
        <div>Footwear</div>
        <div>Accesories</div>
        <div>Tops</div>
        <div>Bottoms</div>
      </div>
      <div class="links">
        <h3>Company</h3>
        <div>Privacy Policy</div>
        <div>Terms of Service</div>
        <div>Customer Care</div>
      </div>
      <div class="icons">
        <a href="https://github.com/Ochoja/shopDADE">
          <Icon icon="flowbite:x-solid"></Icon>
        </a>
        <a href="https://github.com/Ochoja/shopDADE">
          <Icon icon="mdi:instagram"></Icon>
        </a>
        <a href="https://github.com/Ochoja/shopDADE">
          <Icon icon="ant-design:facebook-outlined"></Icon>
        </a>
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  color: #fff;
  background: $primary-color;
  padding: 20px 0 8px 0;
  font-weight: 300;

  .items {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 10px;
    @include grid-width;

    .brand {
      max-width: 24.5em;

      p {
        font-size: 0.8em;
      }
    }

    .links {
      * {
        margin-bottom: 5px;
      }
    }

    .icons {
      display: flex;
      gap: 8px;

      a {
        color: #fff;
        font-size: 1.8em;
      }
    }
  }
}
</style>
