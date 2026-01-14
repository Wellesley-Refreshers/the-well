<template>
  <header>
    <div class="header-grid">
      <h1 class="title">⛲ The Well</h1>
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
    display: flex;
    justify-content: space-around;
    align-items: center;

    height: 100%;
  }

  .title {
    display: block;
    text-align: center;
    font-size: 3em;
    font-family: var(--display-font);
    /* margin: 0; */
    color: white;
  }
</style>