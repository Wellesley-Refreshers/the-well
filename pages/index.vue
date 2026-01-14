<template>
  <Header/>

  <div class="main-container">
    <div class="calendar-container">
      <Calendar />
    </div>

    <div class="search-container">
      <Search />
    </div>
  </div>
</template>

<style scoped>
  .main-container {
    display: flex;
    flex-flow: row-reverse;
    flex-wrap: wrap;

    height: 85vh;
    max-width: 100vw;

    padding: 1em;
  }

  .calendar-container {
    flex-grow: 1000;
  }

  .search-container {
    min-width: 20rem;
    width: 25%;
    height: 100%;
    flex-grow: 1;
  }
</style>
