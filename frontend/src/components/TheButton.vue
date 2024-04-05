<script setup>
import { Icon } from '@iconify/vue'
// import { useRouter } from 'vue-router'

// const router = useRouter()

const props = defineProps({
  size: String,
  icon: String,
  type: String,
  to: String,
  query: Object
})

// const goToRoute = (route, query = null) => {
//   if (query) {
//     router.push({ path: route, query: query })
//   } else {
//     router.push(route)
//   }
// }
</script>

<template>
  <!-- Wide Secondary -->
  <button v-if="props.size == 'wide' && props.type == 'secondary'" class="wide secondary">
    <Icon v-if="props.icon" :icon="props.icon" class="icon"></Icon>
    <slot>Button</slot>
  </button>

  <!-- Wide Primary -->
  <button v-else-if="props.size == `wide`" class="wide">
    <Icon v-if="props.icon" :icon="props.icon" class="icon"></Icon>
    <slot>Button</slot>
  </button>

  <!-- Big Secondary -->
  <button v-else-if="props.size == 'big' && props.type == 'secondary'" class="big secondary">
    <Icon v-if="props.icon" :icon="props.icon" class="icon-big"></Icon>
    <slot>Button</slot>
  </button>

  <!-- Big Primary -->
  <button v-else-if="props.size == `big`" class="big">
    <Icon v-if="props.icon" :icon="props.icon" class="icon-big"></Icon>
    <slot>Button</slot>
  </button>

  <!-- Regular Secondary -->
  <button v-else-if="props.size == 'secondary'" class="secondary">
    <Icon v-if="props.icon" :icon="props.icon" class="icon"></Icon>
    <slot>Button</slot>
  </button>

  <!-- Regular Primary -->
  <button v-else>
    <Icon v-if="props.icon" :icon="props.icon" class="icon"></Icon>
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
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  cursor: pointer;
}

.secondary {
  border: 1px solid $primary-color;
  background: none;
  color: $primary-color;
}

.wide {
  padding: 8px 50px;
  font-weight: 600;
}

.big {
  font-size: 1.2em;
  min-width: 20em;
  padding: 12px 0;
}

.secondary.big {
  border: 2px solid $primary-color;
}

.icon-big {
  font-size: 1.4em;
}
</style>
