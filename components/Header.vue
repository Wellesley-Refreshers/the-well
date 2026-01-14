<template>
  <header>
    <div class="header-title">
      <h1 class="title">The Well</h1>
    </div>
  </header>
</template>

<style scoped>
  header {
    background-color: var(--main-color);
    width: 100%;
    height: 5em;
    margin: 0;
  }

  

  .header-title {
    height: 100%;
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

  .schedule-changer-container {
    position: absolute;
    top: 1em;
    left: 1em;
    height: 80%;
  }
</style>