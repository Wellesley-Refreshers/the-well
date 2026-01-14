<template>
  <header>
    <div class="header-grid">
      <div class="header-schedule">
        <ScheduleChanger/>
      </div>

      <div class="header-title">
        <h1 class="title">The Well</h1>
      </div>

      <div class="header-darkmode">

      </div>
    </div>
  </header>
</template>

<style scoped>
  header {
    /* position: absolute; */
    /* top: 0; */

    background-color: var(--main-color);
    width: 100%;
    height: 5em;
    margin: 0;
  }

  .header-grid {
    display: grid;
    grid-template-columns: 1fr 10fr 1fr;

    height: 100%;
  }

  .header-title {
    display: flex;
    align-items: center;
    justify-items: center;
    justify-content: center;
  }

  .title {
    display: block;
    text-align: center;
    font-size: 3em;
    font-family: var(--display-font);
    margin: 0;
    color: white;
  }
</style>