<template>
  <Header/>

  <div class="main-container">
    <div class="calendar-container">
      <Calendar />
    </div>
    
    <div class="search-container">
      <Search />
    </div>

    <div class="schedule-changer-container">
      <ScheduleChanger />
    </div>
  </div>

  
</template>

<style scoped>
  .main-container {
    padding-top: 1em;
  }

  .calendar-container {
    /* position: absolute; */
    top: 5vh;
    left: 5vw;
    width: 90%;
    height: 80%;
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
