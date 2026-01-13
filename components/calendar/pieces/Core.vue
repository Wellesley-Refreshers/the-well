<script setup>
import { currentCrnColors, currentSessions } from '../../../composables/useSchedules';

import Session from './Session.vue';
import HourLines from './HourLines.vue';
import DayOfWeekHeader from './DayOfWeekHeader.vue';

const selectedSectionCrn = ref("");

const headerHeight = "3em";
</script>

<template>
  <DayOfWeekHeader :height="headerHeight" />

  <div class="calendar-core" :style="{'height': -headerHeight}">
    <HourLines />
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
    position: relative;
    height: 100%;
  }
</style>