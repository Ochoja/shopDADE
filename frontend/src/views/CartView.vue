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
      <div v-for="(item, index) in items" :key="index" class="item">
        <input type="checkbox" v-model="item.selected" />
        <div class="other">
          <div class="img">
            <img :src="item.image" alt="" />
          </div>
          <div class="text">
            <h2>${{ item.name }}</h2>
            <div class="properties">
              <select name="size" id="size" v-if="item.sizes">
                <option value="size" v-for="(size, index) in item.sizes" :key="index">
                  {{ size }}
                </option>
              </select>
            </div>
            <h2>${{ item.price }}</h2>
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

  .cartItems {
    .item {
      display: flex;
      gap: 16px;
      margin-bottom: 16px;

      h2 {
        font-weight: 600;
      }

      .other {
        display: flex;
        gap: 12px;

        .text {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          padding: 20px 0;
        }
      }

      img {
        height: 200px;
        width: 200px;
      }
    }
  }
}
</style>
