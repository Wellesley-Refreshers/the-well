<script setup>
  const props = defineProps({
    dayOfWeek: String,
  })

  function getDayOfWeekDisplay(dayOfWeek) {
    switch (dayOfWeek) {
      case "M":
        return "Mo.";
      case "T":
        return "Tu.";
      case "W":
        return "We.";
      case "R":
        return "Th.";
      case "F":
        return "Fr.";
    }
  }

  const dayOfWeekDisplay = getDayOfWeekDisplay(props.dayOfWeek);
</script>

<template>
  <div class="day-of-week-label-container">
    <div class="day-of-week-label">
      {{ dayOfWeekDisplay }}
    </div>
  </div>
</template>

<style scoped>
  .day-of-week-label-container {
    padding: .5em 1em;
  }

  .day-of-week-label {
    /* To center text vertically */
    display: flex;
    align-items: center;
    justify-content: center;

    background-color: var(--background-color-darker);
    border-radius: 3em;

    width: 100%;
    height: 100%;

    font-size: 1.5em;
    font-weight: 700;
    color: var(--main-color);

/* 
    width: 50%;
    text-align: center;
    height: 150%; */
  }
</style>