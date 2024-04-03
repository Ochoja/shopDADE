<script setup>
import { ref, watch } from 'vue'
import { useCartStore } from '@/stores/cart'
import { storeToRefs } from 'pinia'

const store = useCartStore()
const { items } = storeToRefs(store)
const { selectAll } = store
const { checkItems } = store

const allSelected = ref(false)
const allChecked = ref(false)

// Logic to check and uncheck items
watch(allSelected, () => {
  if (checkItems() == false && allSelected.value == true) {
    selectAll(allSelected.value)
  } else if (checkItems() == true && allSelected.value == false) {
    selectAll(allSelected.value)
  }
})

watch(items.value, () => {
  if (checkItems()) {
    allSelected.value = true
  } else {
    allSelected.value = false
  }
})
</script>

<template>
  <main>
    <div class="heading">
      <input
        type="checkbox"
        v-model="allSelected"
        @clicked="allChecked.value = !allChecked.value"
      />
      <h1>Shopping Cart</h1>
    </div>

    <div class="cartItems">
      <div v-for="(item, index) in items" :key="index">
        <input type="checkbox" v-model="item.selected" />
        <div>
          <div class="img">
            <img :src="item.image" alt="" />
          </div>
          <div class="other">
            <h2>{{ item.name }}</h2>
            {{ item.selected }}
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  @include grid-width;

  .heading {
    display: flex;
    gap: 10px;
  }
}
</style>
