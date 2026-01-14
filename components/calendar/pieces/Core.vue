<script setup>
import DayHeader from './DayHeader.vue';
import DayColumn from './DayColumn.vue';

const daysOfWeek = ["M", "T", "W", "R", "F"];

const selectedCrn = ref("");
</script>

<template>
  <div class="calendar-core">
    <!-- Empty corner spot -->
    <div class="calendar-corner"></div>

    <!-- Day of week labels -->
    <DayHeader v-for="dayOfWeek of daysOfWeek" :dayOfWeek="dayOfWeek" />

    <!-- Space for hour labels -->
    <div></div>

    <!-- Day of week columns -->
    <DayColumn
      v-for="dayOfWeek of daysOfWeek"
      :dayOfWeek="dayOfWeek"
      :selectedCrn="selectedCrn"
      @crnHoverChange="(crn) => {selectedCrn = crn}"
    />
  </div>
</template>

<style scoped>
  .calendar-core {
    display: grid;
    grid-template-columns: 4em repeat(5, 5fr);
    grid-template-rows: 1fr 12fr;
    gap: 2em 0;

    height: 100%;
    width: 100%;

    border: .25em solid var(--main-color);
    border-radius: 2em;
    padding: 1em 1em 2em 1em;
  }
</style>