<script setup>
  const headerHeight = "5em";
  const mainHeight = `calc(100vh - ${headerHeight} - 3em)`; // idk why the extra 3em is needed exactly but whatever
</script>

<template>
  <div class="all-container">
    <div class="header-container" :style="{height: headerHeight}">
      <Header />
    </div>

    <div class="main-container" :style="{height: mainHeight}">
      <div class="draft-area-container">
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
  </div>
</template>

<style scoped>
  .all-container {
    display: flex;
    flex-direction: column;

    gap: 1em;
  }

  .main-container {
    display: flex;
    flex-flow: row-reverse wrap;

    padding: 0 1rem;

    flex-grow: 10;

    /* Helps on thinner screens, when the search goes under the calendar */
    row-gap: 1em;
  }

  .draft-area-container {
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
