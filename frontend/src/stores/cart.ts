import { reactive } from 'vue'
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
      sizes: [6, 7, 8, 9],
      selected_size: 6,
      price: 2332,
      quantity: 5,
      selected: false,
      image:
        'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
    },

    {
      id: 26,
      name: 'Gold Wrist Watch',
      price: 2332,
      quantity: 5,
      selected: false,
      image:
        'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
    }
  ])

  function addToCart(item: item) {
    items.push(item)
  }

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

  return { items, addToCart, selectAll, checkItems }
})
