<script setup></script>

<template>
  <button>
    <slot>Button</slot>
  </button>
</template>

<style lang="scss" scoped>
button {
  border-radius: 40px;
  padding: 8px 25px;
  border: none;
  color: #fff;
  background: $primary-color;
  cursor: pointer;
}
</style>
