<script setup>
import { dayStartHour, dayEndHour } from '../../../composables/dayLimits';

function formatHour(hour) {
  let meridian = "m";
  if (hour < 12) {
    meridian = "a" + meridian;
  } else {
    meridian = "p" + meridian;
  }

  if (hour > 12) {
    hour -= 12;
  }

  return `${hour}${meridian}`;
}

var hourRange = dayEndHour - dayStartHour;
</script>

<template>
  <div class="hour-lines">
    <div class="hour-line" v-for="n in hourRange + 1">
      <div class="hour-text">
        {{ formatHour(dayStartHour + n - 1) }}
      </div>
    </div>
  </div>
</template>

<style scoped>
  .hour-lines {
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    display: flex;
    height: 100%;
  }

  .hour-line {
    border-top: 1px solid gray;
    margin: 0;
    width: 100%;
    height: 0;
  }

  .hour-text {
    text-align: right;
    position: relative;
    top: -.75em;
    left: -101%;
  }

</style>
