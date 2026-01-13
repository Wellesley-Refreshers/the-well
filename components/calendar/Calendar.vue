<script setup>
import Core from './pieces/Core.vue';
import DayOfWeekHeader from './pieces/DayOfWeekHeader.vue';
</script>

<template>
  <div class="calendar-main-container">
    <div class="day-of-week-container">
      <DayOfWeekHeader/>
    </div>
    <div class="calendar-core-container">
      <Core/>
    </div>
  </div>
</template>

<style scoped>
  .calendar-main-container {
    display: flex;
    flex-direction: column;

    /* Left gets extra padding for hour annotations */
    padding: 1em 2em 1em 5em;

    height: 100%;
  }

  .day-of-week-container {
    height: 5em;
  }

  .calendar-core-container {
    height: 100% - 5em;
  }
</style>