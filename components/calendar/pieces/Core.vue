<script setup>
import { currentCrnColors, currentSessions } from '../../../composables/useSchedules';

import Session from './Session.vue';
import HourLines from './HourLines.vue';

const selectedSectionCrn = ref("");
</script>

<template>
  <div class="calendar-core">
    <HourLines/>

    <Session
      v-for="session in currentSessions"
      :key="session.crn"
      :session="session"
      :selected-section-crn="selectedSectionCrn"
      :color="currentCrnColors[session.crn]"
      @becomeHovered="(event) => {selectedSectionCrn = session.crn}"
      @becomeUnhovered="(event) => {selectedSectionCrn = ''}"
    />
  </div>
</template>

<style scoped>
  .calendar-core {
    position: absolute;
    width: calc(100% - 7em); /* accounts for spacing around, hour labels, etc. */
    height: 80%;
  }
</style>