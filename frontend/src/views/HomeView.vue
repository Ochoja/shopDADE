<script setup>
import Button from '../components/TheButton.vue'
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
    margin-bottom: 60px;

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

    p {
      width: 50%;
      margin: auto;
    }
  }
}
</style>
