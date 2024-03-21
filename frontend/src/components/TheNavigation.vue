<script setup>
import { Icon } from '@iconify/vue'
</script>

<template>
  <nav>
    <div class="logo">shopDADE</div>
    <div class="search">
      <div class="category">
        <div class="name">All Category <Icon icon="raphael:arrowdown"></Icon></div>
      </div>
      <div class="search-input">
        <input type="text" placeholder="Browse your favorite products" />
      </div>
      <div class="btn">
        <Icon icon="mingcute:search-line" class="icon" />
      </div>
    </div>
    <div class="user">
      <div class="cart">
        <div class="text">Cart</div>
        <div class="icon"><Icon icon="mdi:cart"></Icon></div>
      </div>
      <div>
        <div class="user">Daniel Ochoja</div>
        <div class="image">
          <img src="" alt="" />
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss" scoped>
nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  @include grid-width;
  margin-top: 20px;
  margin-bottom: 20px;

  .search {
    display: flex;
    align-items: center;
    border: 1px solid $primary-color;
    padding: 7px;
    border-radius: 40px;
    font-weight: 600;
    font-size: 0.9em;

    &-input {
      input {
        margin-left: 10px;
        border: none;
        width: 25em;
      }

      input:focus {
        border: none;
        outline: none;
      }
    }

    .category {
      cursor: pointer;
    }

    .category .name {
      display: flex;
      align-items: center;
      gap: 6px;
      padding-left: 10px;
      padding-right: 8px;
      border-right: 2px solid;
    }

    .btn {
      display: flex;
      justify-content: center;
      align-items: center;
      background: $primary-color;
      padding: 8px 0;
      border-radius: 40px;
      width: 4em;

      .icon {
        color: #fff;
        font-size: 1.5em;
      }
    }
  }

  .user {
    display: flex;
    gap: 16px;
    font-weight: 700;

    .cart {
      display: flex;
      align-items: center;
      gap: 5px;

      .icon {
        font-size: 1.8em;
      }
    }
  }
}
</style>
