<script setup>
import Button from '../components/TheButton.vue'
import Product from '../components/ProductCard.vue'

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
  },
  {
    id: 5,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 6,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 7,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  },
  {
    id: 8,
    product_name: 'Winter Jacket',
    price: 55.99,
    image:
      'https://th.bing.com/th/id/R.3e7489a038bb6747ed2a4e7e6c0c8560?rik=V4nlkcvS7y5qrw&pid=ImgRaw&r=0'
  }
]
</script>

<template>
  <main>
    <div class="hero">
      <div class="content">
        <div class="text">
          Elevate your everyday style effortlessly with <span class="red">shopDADE</span>. Discover
          a curated selection of sophisticated yet versatile gentlemen and lady's official and
          casual wears tailored for the modern working class.
        </div>
        <div class="btn">
          <Button>Start Shopping</Button>
        </div>
      </div>
    </div>

    <section class="featured">
      <h1>New Arrivals</h1>
      <p>
        Introducing our latest arrivals, meticulously curated to elevate your wardrobe with fresh
        sophistication and style
      </p>

      <section class="products">
        <Product v-for="product in products" :key="product.id" :product="product"></Product>
      </section>

      <Button type="wide">See All</Button>
    </section>

    <section class="collection"></section>
  </main>
</template>

<style lang="scss" scoped>
main {
  @include grid-width;

  h1 {
    font-size: 2em;
  }

  .hero {
    display: flex;
    align-items: center;
    padding-left: 40px;
    color: #fff;
    height: 70vh;
    width: 100%;
    background: url('../assets/hero.png') center no-repeat;
    background-size: cover;
    border-radius: 10px;
    margin-bottom: 80px;

    .content {
      width: 55%;

      .text {
        font-size: 1.7em;
        margin-bottom: 10px;

        .red {
          color: $primary-color;
          font-weight: 700;
        }
      }
    }
  }

  .featured {
    text-align: center;
    margin-bottom: 80px;

    p {
      width: 50%;
      margin: auto;
    }
  }

  .products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(16em, 1fr));
    grid-auto-rows: auto;
    column-gap: 25px;
    row-gap: 28px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 30px;
  }

  @media screen and (max-width: 650px) {
    .products {
      grid-template-columns: repeat(auto-fit, minmax(13em, 1fr));
    }
  }
}
</style>
