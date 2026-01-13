<script setup>
import { currentScheduleName, schedules, switchToSchedule, makeNewSchedule, removeSchedule } from '../composables/useSchedules';

const showMenu = ref(false);
const showSchedules = ref(false);

function toggleMenu() {
  showMenu.value = !showMenu.value;
}

function toggleSchedulesMenu() {
  showSchedules.value = !showSchedules.value;
}
</script>

<template>
  <button @click="toggleMenu()">{{ currentScheduleName }}</button>

  <div v-if="showMenu">
    <button @click="toggleSchedulesMenu()">Switch schedule...</button>
    <button @click="removeSchedule()">Delete this schedule</button>
    <button @click="makeNewSchedule()">Make new schedule</button>
  </div>

  <div v-if="showSchedules">
    <button v-for="[i, schedule] in schedules.entries()" @click="switchToSchedule(i); toggleSchedulesMenu()" >{{ schedule.name }}</button>
  </div>
</template>

<style scoped>

</style>
