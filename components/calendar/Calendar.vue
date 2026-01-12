<script setup>
import { currentSchedule, currentSessions } from '../../composables/useSchedules';
import { dayStartHour, dayEndHour } from '../../composables/dayLimits';

import Session from './pieces/Session.vue';

const selectedSectionCrn = ref("");

var hourRange = dayEndHour - dayStartHour;
</script>

<template>
  <div class="calendar">
    <div class="hour-lines">
      <div class="hour-line" v-for="n in hourRange + 1"></div>
    </div>

    <Session
      v-for="session in currentSessions"
      :key="session.crn"
      :session="session"
      :selected-section-crn="selectedSectionCrn"
      :color="currentSchedule[session.crn]"
      @becomeHovered="(event) => {selectedSectionCrn = session.crn}"
      @becomeUnhovered="(event) => {selectedSectionCrn = ''}"
    />
  </div>
</template>

<style scoped>
  .hour-lines {
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    display: flex;
    height: 100%;
  }

  .hour-line {
    border-top: 1px solid gray;
    width: 100%;
  }

  .hour-block {
    height: 100%;
    border-style: solid;
    border-color: gray;
    border-width: 1px 0px;
  }

  .v-event-timed {
    border-radius: 500px !important;
  }
</style>
