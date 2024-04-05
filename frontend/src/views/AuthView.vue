<script setup>
import { ref, computed, watchEffect } from 'vue'
import Button from '@/components/TheButton.vue'
import { RouterLink, useRouter } from 'vue-router'
import axios from 'axios'
import { Icon } from '@iconify/vue/dist/iconify.js'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

const store = useUserStore()
const { user_mail } = storeToRefs(store)

const name = ref('')
const mail = ref('')
const password = ref('')
const confirm_password = ref('')
const match = computed(() => {
  return !(password.value == confirm_password.value)
})
const checkFields = ref(true)
const checkLogin = ref(true)
const loading = ref(false)
const correctLogin = ref(false)

const router = useRouter()

watchEffect(() => {
  if (mail.value == '' || password.value == '') {
    checkLogin.value = true
  } else {
    checkLogin.value = false
  }
})

watchEffect(() => {
  if (
    name.value == '' ||
    mail.value == '' ||
    password.value == '' ||
    confirm_password.value == ''
  ) {
    checkFields.value = true
  } else {
    checkFields.value = false
  }
})

defineProps({
  type: String
})

async function createAccount() {
  try {
    if (match.value || checkFields.value) return
    else {
      loading.value = true
      const formData = {
        fullname: name.value,
        email: mail.value,
        password: password.value
      }
      console.log(formData)

      const response = await axios.post('https://shopdade.onrender.com/register', formData)
      console.log(response)
      loading.value = false
      name.value = ''
      password.value = ''
      confirm_password.value = ''
      mail.value = ''
      router.push('/auth/login')
    }
  } catch (error) {
    loading.value = false
    console.log(error)
  }
}

async function login() {
  try {
    if (checkLogin.value) return
    else {
      loading.value = true
      const formData = { email: mail.value, password: password.value }
      console.log(formData)

      const response = await axios.post('https://shopdade.onrender.com/login', formData)
      console.log(response)
      loading.value = false
      router.push('/')
      user_mail.value = mail.value
    }
  } catch (error) {
    correctLogin.value = true
    loading.value = false
    console.log(error)
  }
}
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

        <form>
          <label for="name">Full Name*</label>
          <input type="e-mail" placeholder="John Doe" id="name" required v-model="name" />

          <label for="mail">Email*</label>
          <input type="e-mail" id="mail" placeholder="John Doe" required v-model="mail" />

          <label for="password">Password*</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
            required
            v-model="password"
          />

          <label for="confirm-password">Retype Password*</label>
          <input
            type="password"
            id="confirm-password"
            placeholder="Enter your password"
            required
            v-model="confirm_password"
          />

          <div v-if="match" class="warning">Passwords do not match</div>
          <div v-if="checkFields" class="warning">Fill All fields</div>
        </form>

        <div class="action">
          <Button size="big" @click="createAccount">
            <Icon v-if="loading" class="icon" icon="eos-icons:three-dots-loading" />
            <span v-else>Create Account</span>
          </Button>
          <p>Already have an account? <RouterLink to="/auth/login">Sign In</RouterLink></p>
        </div>
      </div>

      <div v-else>
        <h1>Sign In</h1>
        <p>Welcome back! Enter your details</p>

        <form>
          <label for="mail">Email</label>
          <input type="e-mail" id="mail" placeholder="Enter your email" v-model="mail" required />

          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
            v-model="password"
            required
          />
          <div v-if="checkLogin" class="warning">Please fill the form</div>
          <div v-if="correctLogin" class="warning">Email or Password Incorrect</div>
        </form>

        <div class="action">
          <Button size="big" @click="login">
            <Icon v-if="loading" class="icon" icon="eos-icons:three-dots-loading" />
            <span v-else>Sign In</span>
          </Button>
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

    .warning {
      font-weight: 600;
      color: $primary-color;
      position: relative;
      top: -6px;
    }

    .action {
      text-align: center;
      margin-top: 20px;

      .icon {
        font-size: 1.5em;
      }

      p {
        margin-top: 8px;
      }
    }
  }

  .img {
    background: url('https://res.cloudinary.com/dmnzisj8k/image/upload/v1711652773/shopDADE/q4r2ucsvmz77veyc06nw.png')
      no-repeat;
    background-position: center;
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
