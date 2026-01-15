<template>
  <Header/>

  <div class="all-container">
    <div class="main-container">
      <div class="schedule-select-container">
        <ScheduleChanger/>
      </div>

      <div class="calendar-container">
        <Calendar />
      </div>
    </div>

    <div class="search-container">
      <Search />
    </div>
  </div>
</template>

<style scoped>
  .all-container {
    display: flex;
    flex-flow: row-reverse wrap;

    height: 85vh;
    max-width: 100vw;

    padding: 1em;
  }

  .main-container {
    display: flex;
    flex-flow: column;
    gap: 1rem;

    flex-grow: 1000;
  }

  .schedule-select-container {
    display: flex;
    flex-direction: row-reverse;
  }

  .calendar-container {
    flex-grow: 10;
  }

  .search-container {
    min-width: 20rem;
    width: 25%;
    height: 100%;
    flex-grow: 1;
  }
</style>
