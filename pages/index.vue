<template>
  <div class="calendar-container">
    <Calendar />
  </div>

  <ScheduleChanger />
  
  <div class="search-container">
    <Search />
  </div>
</template>

<style scoped>
  .calendar-container {
    position: absolute;
    top: 5em;
    left: 5em;
    width: 50em;
    height: 50em;
    margin-bottom: 5em;
  }

  .search-container {
    position: absolute;
    top: 60em;
  }
</style>
