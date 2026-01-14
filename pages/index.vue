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
    flex-flow: row-reverse;
    flex-wrap: wrap;

    height: 85vh;
    max-width: 100vw;

    padding: 1em;
  }

  .main-container {
    flex-grow: 1000;
  }

  .schedule-select-container {
    display: flex;
    flex-direction: row-reverse;
  }

  .search-container {
    min-width: 20rem;
    width: 25%;
    height: 100%;
    flex-grow: 1;
  }
</style>
