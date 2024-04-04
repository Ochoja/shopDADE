<script setup>
import { ref, watch } from 'vue'
import { useCartStore } from '@/stores/cart'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'
import Button from '@/components/TheButton.vue'

const store = useCartStore()
const { items, subtotal, tax, total } = storeToRefs(store)
const { selectAll } = store
const { checkItems } = store
const { changeQuantity } = store

const allSelected = ref(true)
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
      <div>
        <div v-for="(item, index) in items" :key="index" class="item">
          <input type="checkbox" v-model="item.selected" />
          <div class="other">
            <div class="img">
              <img :src="item.image" alt="" />
            </div>
            <div class="text">
              <h2>{{ item.name }}</h2>
              <div class="properties">
                <select
                  name="size"
                  id="size"
                  v-if="item.sizes"
                  v-model="item.selected_size"
                  class="custom-select"
                >
                  <option :value="size" v-for="(size, index) in item.sizes" :key="index">
                    Size {{ size }}
                  </option>
                </select>

                <div class="quantity">
                  <Icon
                    icon="ic:round-minus"
                    @click="changeQuantity(item.id, 'minus')"
                    class="icon"
                  ></Icon>
                  {{ item.quantity }}
                  <Icon
                    icon="ic:round-plus"
                    @click="changeQuantity(item.id, 'plus')"
                    class="icon"
                  ></Icon>
                </div>
              </div>
              <h2>${{ item.price }}</h2>
            </div>
          </div>
        </div>
      </div>
      <div class="summary">
        <h3>Order Summary</h3>
        <div class="item">
          <div>Subtotal</div>
          <div class="amount">${{ subtotal.toFixed(2) }}</div>
        </div>
        <div class="item">
          <div>Tax</div>
          <div class="amount">${{ tax.toFixed(2) }}</div>
        </div>
        <div class="item">
          <div>Total</div>
          <div class="amount">${{ total.toFixed(2) }}</div>
        </div>

        <Button size="big">Checkout</Button>
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
    margin-top: 22px;
    display: grid;
    grid-template-columns: 2fr 1fr;

    .item {
      display: flex;
      gap: 16px;
      margin-bottom: 24px;

      h2 {
        font-weight: 600;
      }

      .other {
        display: flex;
        gap: 12px;

        .properties {
          display: flex;
          gap: 16px;

          select {
            // appearance: none;
            // -webkit-appearance: none;

            font-size: 1.15em;
            padding: 8px;
            background-color: #fff;
            border: 1px solid #000;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
          }
        }

        .text {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          padding: 20px 0;

          .quantity {
            display: flex;
            align-items: center;
            gap: 8px;
            border-radius: 5px;
            padding: 8px 12px;
            font-size: 1.15em;
            font-weight: 600;
            border: 1px solid #000;

            .icon {
              font-size: 1.3em;
              cursor: pointer;
            }
          }
        }
      }

      img {
        height: 200px;
        width: 200px;
        border-radius: 10px;
      }
    }

    .summary {
      border: 1px solid $primary-color;
      border-radius: 10px;
      padding: 12px 16px;
      height: min-content;

      h3 {
        text-align: center;
        margin-bottom: 8px;
      }

      .item {
        display: flex;
        justify-content: space-between;

        .amount {
          font-weight: 600;
        }
      }

      button {
        width: 100%;
      }
    }
  }
}
</style>
