<script setup>
import { Icon } from '@iconify/vue'
defineProps({
  type: String,
  icon: String
})
</script>

<template>
  <button v-if="type == `wide`" class="wide">
    <Icon v-if="icon" :icon="icon"></Icon>
    <slot>Button</slot>
  </button>
  <button v-else-if="type == `big`" class="big">
    <Icon v-if="icon" :icon="icon"></Icon>
    <slot>Button</slot>
  </button>
  <button v-else>
    <Icon v-if="icon" :icon="icon"></Icon>
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

.wide {
  padding: 8px 50px;
  font-weight: 600;
}
</style>
