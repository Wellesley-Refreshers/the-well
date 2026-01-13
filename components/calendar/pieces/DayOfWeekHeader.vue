<template>
  <div class="day-of-week-header">
    <div class="day-of-week-columns">
      <div class="day-of-week-label-container"><div class="day-of-week-label">Mo.</div></div>
      <div class="day-of-week-label-container"><div class="day-of-week-label">Tu.</div></div>
      <div class="day-of-week-label-container"><div class="day-of-week-label">We.</div></div>
      <div class="day-of-week-label-container"><div class="day-of-week-label">Th.</div></div>
      <div class="day-of-week-label-container"><div class="day-of-week-label">Fr.</div></div>
    </div>
  </div>
</template>

<style scoped>
  .day-of-week-header {
    margin-top: 1em;
  }

  .day-of-week-columns {
    display: flex;
    flex-direction: row;
  }

  .day-of-week-label-container {
    display: flex;
    justify-content: center;

    font-size: 1.25em;

    width: 20%;
  }

  .day-of-week-label {
    /* To center text vertically */
    display: flex;
    align-items: center;
    justify-content: center;

    background-color: var(--background-color-darker);
    border-radius: 3em;


    width: 50%;
    text-align: center;
    height: 150%;
  }
</style>