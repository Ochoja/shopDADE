<script setup>
import Button from '@/components/TheButton.vue'
import { RouterLink } from 'vue-router'

defineProps({
  type: String
})
</script>

<template>
  <main>
    <div class="text">
      <div class="logo">
        <RouterLink to="/">shopDADE</RouterLink>
      </div>

      <div v-if="type == 'register'">
        <h1>Create an Account</h1>
        <p>Welcome back! Enter your details</p>

        <form action="">
          <label for="">Full Name*</label>
          <input type="e-mail" placeholder="John Doe" required />

          <label for="">Full Name*</label>
          <input type="e-mail" placeholder="John Doe" required />

          <label for="">Password*</label>
          <input type="password" placeholder="Enter your password" required />

          <label for="">Retype Password*</label>
          <input type="e-mail" placeholder="Enter your password" required />
        </form>

        <div class="action">
          <Button size="big">Create Account</Button>
          <p>Already have an account? <RouterLink to="/auth/login">Sign In</RouterLink></p>
        </div>
      </div>

      <div v-else>
        <h1>Sign In</h1>
        <p>Welcome back! Enter your details</p>

        <form action="">
          <label for="">Email</label>
          <input type="e-mail" placeholder="Enter your email" required />

          <label for="">Password</label>
          <input type="password" placeholder="Enter your password" required />
        </form>

        <div class="action">
          <Button size="big">Create Account</Button>
          <p>
            Don't have an account? <RouterLink to="/auth/register">Sign Up For Free</RouterLink>
          </p>
        </div>
      </div>
    </div>
    <div class="img"></div>
  </main>
</template>

<style lang="scss" scoped>
main {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: 100vh;

  .text {
    border-radius: 0 20px 20px 0;
    position: relative;
    right: -15px;
    padding: 25px 15px 0 0;
    background: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;

    h1,
    p {
      text-align: center;
    }

    h1 {
      font-weight: 600;
      line-height: 1.2em;
      margin-top: 20px;
    }

    a {
      text-decoration: none;
      color: $primary-color;
      font-weight: 700;
    }

    .logo a {
      font-weight: 400;
    }

    form {
      margin-top: 24px;
    }

    label {
      display: block;
      margin-bottom: 2px;
      font-size: 1em;
    }

    input {
      border-radius: 10px;
      padding: 12px 8px;
      border: 1px solid;
      min-width: 24em;
      margin-bottom: 12px;
    }

    input:focus {
      outline: $primary-color;
      border: 2px solid $primary-color;
    }

    .action {
      text-align: center;
      margin-top: 20px;

      p {
        margin-top: 8px;
      }
    }
  }

  .img {
    background: url('https://res.cloudinary.com/dmnzisj8k/image/upload/v1711652773/shopDADE/q4r2ucsvmz77veyc06nw.png')
      center no-repeat;
    background-size: cover;
  }
}

@media screen and (max-width: 800px) {
  main {
    grid-template-columns: 1fr;

    .text {
      position: static;
      padding: 25px 0 0 0;
    }

    .img {
      display: none;
    }
  }
}
</style>
