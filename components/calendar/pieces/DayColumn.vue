<script setup>
  import { currentSessions } from "../../../composables/useSchedules";

  import Session from './Session.vue';
  import HourLines from './HourLines.vue';

  const props = defineProps({
    dayOfWeek: String,
    selectedCrn: String,
  })

  function getSessionsForDay(dayOfWeek) {
    let daySessions = [];
    for (const session of currentSessions.value) {
      if (session.dayOfWeek === dayOfWeek) {
        daySessions.push(session);
      }
    }
    
    return daySessions
  }

  const daySessions = computed(() => getSessionsForDay(props.dayOfWeek));
</script>

<template>
  <div class="day-of-week-column">
    <!-- Kinda hacky, but to align labels we simply show them only on the Monday column. -->
    <HourLines :show-hour-labels="dayOfWeek == 'M'"/>

    <Session
      v-for="session in daySessions"
      :key="session.crn"
      :session="session"
      :selected-crn="selectedCrn"
      :color="currentCrnColors[session.crn]"
      @becomeHovered="(event) => {$emit('crnHoverChange', session.crn)}"
      @becomeUnhovered="(event) => {$emit('crnHoverChange', '')}"
    />
  </div>
</template>

<style scoped>
  .day-of-week-column {
    /* This causes the Sessions to be placed properly relative
    to the height and width of this DayColumn,
    which does not work with position: static or absolute. */
    position: relative;

    height: 100%;
    width: 100%;
  }
</style>