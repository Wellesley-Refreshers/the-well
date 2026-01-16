<script setup>
import { currentScheduleName, schedules, switchToSchedule, makeNewSchedule, removeSchedule, renameSchedule } from '../composables/useSchedules';

const showMenu = ref(false);

const showRenamePopup = ref(false);

function toggleMenu() {
  showMenu.value = !showMenu.value;
}
</script>

<template>
  <div v-if="showRenamePopup" class="popup-overlay" @click="showRenamePopup = false">
    <div class="popup-content" @click.stop>
      <h3 class="popup-caption">Rename {{ currentScheduleName }}:</h3>

      <input class="rename-input" v-model="newName" @keyup.enter="renameSchedule(newName); newName = ''; showRenamePopup = false" />
    </div>
  </div>

  <div class="button main-button" @click="toggleMenu()">
    <div class="current-schedule-display">
      {{ currentScheduleName }}
    </div>

    <div class="dropdown-arrow-container">
      <Icon id="dropdown-arrow" name="raphael:arrowdown" />
    </div>

    <div class="dropdown-menu main-menu" v-if="showMenu">
      <div class="button dropdown-option" v-for="[i, schedule] in schedules.entries()" @click="switchToSchedule(i)" >{{ schedule.name }}</div>
      <hr>
      <div class="button dropdown-option" @click="makeNewSchedule()">Make new schedule</div>
      <div class="button dropdown-option" @click="showRenamePopup = true">Rename schedule</div>
      <div class="button dropdown-option" @click="removeSchedule()">Delete this schedule</div>
    </div>
  </div>
</template>

<style scoped>
  div {
    font-family: var(--readable-font);
  }

  .main-button {
    position: relative;

    font-size: 1.25em;
    display: flex;

    background-color: var(--background-color);
    border: .25em solid var(--main-color);
    border-radius: 1em;
    cursor: pointer;
  }

  .current-schedule-display {
    margin: .5em 1em;
  }

  .main-menu {
    position: absolute;
    top: 8rem;
    right: 1em;
  }

  .dropdown-menu {
    z-index: 1000;
    margin-top: 2em;
    background-color: var(--background-color);
    border: .25em solid var(--main-color);
    border-radius: .5em;
    padding: .5em;
  }

  .dropdown-arrow-container {
    width: 2em;
    height: 100%;
    text-align: center;

    overflow: hidden;

    background-color: var(--main-color);

    /* Slightly hacky way of getting the arrow section on the side to have
    rounded corners along with its container */
    border-radius: 0 .5em .5em 0;
  }

  #dropdown-arrow {
    height: 100%;
    width: 1.5em;

    color: white;
  }

  .dropdown-option {
    padding: .5em;
    border-radius: .5em;
  }

  .button:hover {
    background-color: var(--background-color-darker);
    cursor: pointer;
  }

  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
    background-color: rgba(238, 238, 238, 0.8);
  }

  .popup-content {
    background-color: var(--background-color);
    border: 1em solid var(--main-color);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 1em;
    padding: 2em 1.5em 1.5em;

    border: 3px solid var(--main-color);
    max-width: 90vw;
    max-height: 80vh;
    overflow-y: auto;
    display: block;
    flex-direction: column;
    gap: 1.5em;
  }

  .popup-caption {
    font-size: 2em;
    margin: 0;
    margin-bottom: .5em;
  }

  .rename-input {
    border: .25em solid var(--main-color);
    border-radius: 1em;
    padding: .5em;
    font-size: 1.5em;
  }
</style>
