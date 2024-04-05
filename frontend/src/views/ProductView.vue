<script setup>
import { ref } from 'vue'
import { Icon } from '@iconify/vue/dist/iconify.js'
import { useCartStore } from '@/stores/cart'
import Button from '@/components/TheButton.vue'
import Product from '@/components/ProductCard.vue'

defineProps({
  id: String
})

const store = useCartStore()
const { addToCart } = store

/* Product images and sizes */
const imgs = [
  'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0',
  'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0',
  'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
]
const sizes = [25, 26, 27, 28]

/* Suggested Images and sizes*/
const products = [
  {
    id: 1,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 2,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 3,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 4,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  }
]

/* Change quantity */
const quantity = ref(1)
function changeQuantity(operation) {
  if (operation == 'add') quantity.value++
  else {
    if (quantity.value > 1) quantity.value--
  }
}

/* Change selected size */
let selectedSize = 0
const active = ref(null)

const selectSize = (index) => {
  for (let element of active.value) {
    element.classList.remove('active')
  }
  selectedSize = active.value[index].innerHTML
  active.value[index].classList.add('active')
  console.log(`Selected size: ${selectedSize}`)
}
/* End change selected size */
</script>

<template>
  <main>
    <div class="product-info">
      <div class="images">
        <div class="main-img">
          <img :src="imgs[0]" alt="" />
        </div>
        <div class="more-imgs">
          <img v-for="(img, index) in imgs" :key="index" :src="img" alt="product-img" />
        </div>
      </div>

      <div class="more">
        <h2 class="name">Green Leather Jacket</h2>
        <h2 class="price">$55.99</h2>
        <div class="description">
          Effortlessly elevate your ensemble with our One Button Blazer Jacket. Crafted with
          precision and tailored for sophistication, this versatile piece seamlessly transitions
          from office to evening, adding a touch of refinement to any look. With its classic design
          and impeccable fit, our blazer is a timeless essential for the modern wardrobe
        </div>

        <div class="product-sizes">
          <h3>Size</h3>
          <div class="sizes">
            <div
              class="size"
              v-for="(size, index) in sizes"
              :key="index"
              ref="active"
              @click="selectSize(index)"
            >
              {{ size }}
            </div>
          </div>
        </div>

        <div class="quantity">
          <h3>Quantity</h3>
          <div class="btns">
            <div class="qty-btn" @click="changeQuantity('reduce')">
              <Icon :icon="`ic:round-minus`"></Icon>
            </div>
            <div class="value">{{ quantity }}</div>
            <div class="qty-btn" @click="changeQuantity('add')">
              <Icon :icon="`ic:round-plus`"></Icon>
            </div>
          </div>
        </div>

        <div class="action-btns">
          <div>
            <Button icon="material-symbols:shopping-bag-outline" size="big"> Add to Cart </Button>
          </div>
          <div>
            <Button icon="mdi:heart-outline" size="big" type="secondary">Add to Wishlist</Button>
          </div>
        </div>
      </div>
    </div>

    <div class="suggestion">
      <h1>You May Also Like</h1>

      <div class="items">
        <Product v-for="product in products" :key="product.id" :product="product"></Product>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  @include grid-width;
}

img {
  border-radius: 10px;
}

.product-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 50px;

  @media screen and (max-width: 760px) {
    grid-template-columns: 1fr;
  }

  .images {
    .main-img {
      height: 75vh;
      margin-bottom: 12px;

      img {
        height: inherit;
        width: 100%;
        object-fit: cover;
      }
    }

    .more-imgs {
      display: flex;
      gap: 5px;

      img {
        height: 50px;
        width: 50px;
      }
    }

    @media screen and (max-width: 650px) {
      .main-img {
        height: 50vh;
      }
    }
  }

  h2,
  h3 {
    font-weight: 600;
  }

  h2 {
    margin-bottom: 8px;
  }

  h3 {
    margin-bottom: 5px;
  }

  .description {
    margin-bottom: 20px;
  }

  .qty-btn,
  .size {
    padding: 8px 12px;
    border: 1px solid;
    border-radius: 5px;
    font-weight: 500;
    font-size: 1.2em;
    cursor: pointer;
  }

  .size.active {
    border: 2px solid #daa1a8;
    background: #ef233c;
    color: #fff;
    font-weight: 600;
  }

  .more {
    .sizes {
      margin-bottom: 20px;
      display: flex;
      gap: 5px;
    }

    .quantity {
      .btns {
        display: flex;
        align-items: center;
        gap: 10px;

        input {
          border: none;
          width: 2em;
        }

        input:focus {
          border: none;
          outline: none;
        }

        .qty-btn {
          font-size: 1.5em;
          padding: 11px 9.5px;
        }

        .qty-btn:hover {
          background: $primary-color;
          color: #fff;
        }

        .value {
          font-size: 1.7em;
          font-weight: 500;
        }
      }
    }

    .action-btns {
      margin-top: 30px;

      div {
        margin-bottom: 10px;
      }
    }
  }
}

.suggestion {
  margin-top: 80px;
  margin-bottom: 120px;

  h1 {
    text-align: center;
    margin-bottom: 15px;
  }

  .items {
    @include product-grid;
  }
}
</style>
