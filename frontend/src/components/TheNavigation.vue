<script setup>
import { ref } from 'vue'
import { Icon } from '@iconify/vue'
import { RouterLink } from 'vue-router'

const isLoggedIn = ref(false)
const logInMenu = ref(false)
</script>

<template>
  <nav>
    <div class="logo">
      <RouterLink to="/">shopDADE</RouterLink>
    </div>
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
      <div class="profile" v-if="isLoggedIn">
        <div class="user">Daniel Ochoja</div>
        <div class="img">
          <img
            src="https://th.bing.com/th/id/R.8b167af653c2399dd93b952a48740620?rik=%2fIwzk0n3LnH7dA&pid=ImgRaw&r=0"
            alt="user-image"
          />
        </div>
      </div>
      <div class="profile" v-else @click="logInMenu = !logInMenu">
        <div class="text">Login/Register</div>
        <div><Icon icon="bxs:down-arrow" /></div>
      </div>
    </div>
  </nav>

  <div v-show="logInMenu" class="login-menu">
    <RouterLink to="/auth/login">Login</RouterLink>
    <RouterLink to="/auth/register">Register</RouterLink>
  </div>
</template>

<style lang="scss" scoped>
nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  @include grid-width;
  margin-top: 20px;
  margin-bottom: 20px;

  .logo {
    a {
      color: $primary-color;
    }
  }

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
    gap: 25px;
    font-weight: 700;

    .cart,
    .profile {
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;

      .icon {
        font-size: 1.8em;
      }

      .img {
        height: 2.5em;
        width: 2.5em;
        border-radius: 50%;
        position: relative;
        overflow: hidden;

        img {
          height: 100%;
          width: 100%;
          object-fit: cover;
        }
      }
    }
  }
}
</style>
