<script setup>
import Button from '../components/TheButton.vue'
import Product from '../components/ProductCard.vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

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

      <div class="btn">
        <Button size="wide">See All</Button>
      </div>
    </section>

    <section class="collection">
      <h1>Our Collections</h1>

      <div class="categories">
        <RouterLink
          to=""
          class="regular"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/footwear.png?updatedAt=1711169406807');
          "
          >Footwears</RouterLink
        >
        <RouterLink
          to="/"
          class="long"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/suit.png?updatedAt=1711169407259');
          "
          >Suits</RouterLink
        >
        <RouterLink
          to="/"
          class="regular"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/accesories.png?updatedAt=1711169406591');
          "
          >Accesories</RouterLink
        >
        <RouterLink
          to="/"
          class="long"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/tops.png?updatedAt=1711169407303');
          "
          >Tops</RouterLink
        >
        <RouterLink
          to="/"
          class="long"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/pants.png?updatedAt=1711169407202');
          "
          >Bottoms</RouterLink
        >
        <RouterLink
          to="/"
          class="regular"
          style="
            background-image: url('https://ik.imagekit.io/Ochoja01/shopDADE/jacket.png?updatedAt=1711169406932');
          "
          >Jackets</RouterLink
        >
      </div>
    </section>
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

    @media screen and (max-width: 750px) {
      .content {
        width: 100%;

        .text {
          font-size: 1.5em;
        }
      }
    }
  }

  .featured {
    text-align: center;
    margin-bottom: 80px;

    p {
      width: 50%;
      margin: 0 auto 8px auto;
    }

    @media screen and (max-width: 750px) {
      p {
        width: 95%;
      }
    }

    .btn {
      button {
        margin: auto;
      }
    }
  }

  .products {
    @include product-grid;
    margin-bottom: 30px;
  }

  .collection {
    text-align: center;
    margin-bottom: 100px;

    h1 {
      margin-bottom: 10px;
    }
  }

  .categories {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-auto-rows: auto;
    height: 90vh;
    gap: 12px;

    @media screen and (max-width: 750px) {
      grid-template-columns: 1fr 1fr;
    }

    @media screen and (max-width: 650px) {
      grid-template-columns: 1fr;
      height: auto;
    }

    .regular,
    .long {
      background-size: cover;
      background-repeat: no-repeat;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px;
      text-decoration: none;
      color: #fff;
      font-size: 1.8em;
      font-weight: 600;
    }

    .long {
      grid-row: span 5;
    }

    .regular {
      grid-row: span 3;
    }

    @media screen and (max-width: 750px) {
      .long,
      .regular {
        grid-row: span 3;
        height: 10em;
      }
    }
  }
}
</style>
