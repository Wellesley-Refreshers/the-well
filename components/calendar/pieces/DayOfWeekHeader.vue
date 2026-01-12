<script setup>
const props = defineProps({
  height: String,
});
</script>

<template>
  <div class="calendar-header" :style="{'height': height}">
    <div class="day-of-week-columns">
      <div class="day-of-week-label">Mo.</div>
      <div class="day-of-week-label">Tu.</div>
      <div class="day-of-week-label">We.</div>
      <div class="day-of-week-label">Th.</div>
      <div class="day-of-week-label">Fr.</div>
    </div>
  </div>
</template>

<style scoped>
  .day-of-week-columns {
    display: flex;
    flex-direction: row;
  }

  .day-of-week-label {
    font-size: 1.25em;

    width: 20%;
    /* height: 2em; */
    /* color: white; */

    /* To center text vertically */
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>