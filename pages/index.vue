<template>
  <Header/>

  <div class="main-container">
    <div class="search-container">
      <Search />
    </div>
    
    <div class="calendar-container">
      <Calendar />
    </div>
  </div>
</template>

<style scoped>
  .main-container {
    display: flex;
    height: 85vh;
    max-width: 100vw;

    padding: 1em;
  }

  .calendar-container {
    /* min-width: 50%; */
    flex-grow: 10;
  }

  .search-container {
    /* min-width: 20%; */
    width: 20%;
    height: 100%;
    flex-grow: 1;
    /* border: .5rem solid var(--main-color);
    border-radius: 2rem; */
  }
</style>
