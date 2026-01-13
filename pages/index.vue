<template>
  <!-- <Header /> -->

  <div class="calendar-container">
    <Calendar />
  </div>

  <div class="search-container">
    <Search />
  </div>

  <div class="schedule-changer-container">
    <ScheduleChanger />
  </div>
</template>

<style scoped>
  .calendar-container {
    position: absolute;
    top: 5vh;
    left: 5vw;
    width: 90vw;
    height: 90vh;

    border: .25em solid var(--main-color);
    border-radius: 3em;
  }

  .search-container {
    position: absolute;
    top: 70em;
    width: 30em;
  }

  .schedule-changer-container {
    position: fixed;
    top: 5em;
    right: 5em;
  }
</style>
