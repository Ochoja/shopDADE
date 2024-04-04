import { reactive, computed } from 'vue'
import { defineStore } from 'pinia'

interface item {
  id: number
  name: string
  sizes?: number[]
  price: number
  quantity: number
  selected: boolean
  image: string
  selected_size?: number
}

export const useCartStore = defineStore('cart', () => {
  const items: item[] = reactive([
    {
      id: 34,
      name: 'Leather Jacket',
      sizes: [2, 6, 7, 8, 9],
      selected_size: 6,
      price: 2332,
      quantity: 5,
      selected: true,
      image:
        'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
    },

    {
      id: 26,
      name: 'Gold Wrist Watch',
      price: 2332,
      quantity: 5,
      selected: true,
      image:
        'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
    }
  ])

  // calculate subtotal
  const subtotal = computed(() => {
    let total = 0

    for (let i = 0; i < items.length; i++) {
      if (items[i].selected === true) {
        total += items[i].price * items[i].quantity
      }
    }

    return total
  })

  const tax = computed(() => {
    return subtotal.value * 0.01
  }) // 1% of subtotal

  const total = computed(() => {
    return subtotal.value + tax.value
  })

  function addToCart(item: item) {
    items.push(item)
  }

  // select all items
  function selectAll(status: boolean) {
    items.forEach((product) => {
      product.selected = status
    })
  }

  // Check if all items are selected
  function checkItems() {
    for (let index = 0; index < items.length; index++) {
      if (items[index].selected == false) {
        return false
      }
    }
    return true
  }

  // increase or decrease quantity of item
  function changeQuantity(id: number, operation: string) {
    const index = items.findIndex((object) => object.id === id)

    if (operation == 'minus' && items[index].quantity > 1) {
      items[index].quantity--
    } else if (operation == 'plus') {
      items[index].quantity++
    } else {
      return
    }
  }

  return { items, addToCart, selectAll, checkItems, changeQuantity, subtotal, tax, total }
})
