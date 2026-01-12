<script setup>
import { computed } from "vue";
import { removeClass } from "../../../composables/useSchedules";
import { dayStartMinute, dayEndMinute } from "../../../composables/dayLimits";

import allCourseSections from "../../../data/parsed/currentCourses.json";


const props = defineProps({
  session: Object,
  color: String,
  selectedSectionCrn: String,
})

let dayWidth = 1 / 5;

const overlappingSessions = computed(() => {
  let overlappingSessions = [];

  for (const otherSession of currentSessions.value) {
    const dayOverlaps = props.session.dayOfWeek == otherSession.dayOfWeek;
    const timeOverlaps = !(
      otherSession.end <= props.session.start || otherSession.start >= props.session.end
    );

    if (dayOverlaps && timeOverlaps) {
      overlappingSessions.push(otherSession);
    }
  }

  return overlappingSessions;
});

function getMinutesSinceStartOfDay(day) {
  return 60 * day.getHours() + day.getMinutes();
}

function offsetByDayOfWeek(dayOfWeek) {
  switch(dayOfWeek) {
    case "M":
      return 0 * dayWidth;
    case "T":
      return 1 * dayWidth;
    case "W":
      return 2 * dayWidth;
    case "R":
      return 3 * dayWidth;
    case "F":
      return 4 * dayWidth;
  }
}

let totalMinute = dayEndMinute - dayStartMinute;

// how much of the total height each minute takes up
let fracPerMinute = 1 / totalMinute;

let startMinute = props.session.start - dayStartMinute;
let endMinute = props.session.end - dayStartMinute;
let duration = endMinute - startMinute;

let overlapShift = computed(() => {
  let thisSessionIndex = overlappingSessions.value.findIndex(session => session == props.session);
  return thisSessionIndex * (1 / overlappingSessions.value.length);
});

let outerStyle = computed(() => {
  return {
    "top": `${100 * fracPerMinute * startMinute}%`,
    "left": `${(offsetByDayOfWeek(props.session.dayOfWeek) + overlapShift.value * dayWidth) * 100}%`,
    "width": `${(dayWidth * 100) / overlappingSessions.value.length}%`,
    "height": `${(duration / totalMinute) * 100}%`
  }
});

let innerStyle = computed(() => {
  return {"background-color": props.color, "height": "100%"};
});

let section = allCourseSections[props.session.crn];
let course = `${section.dept} ${section.course_no} - ${section.section_no}`;

</script>

<template>
  <div class="class-block-outer" :style="outerStyle">
    <div
      class="class-block"
      :class="{ active: props.selectedSectionCrn === props.session.crn }"
      :style="innerStyle"
      @mouseover="(event) => $emit('becomeHovered', event)"
      @mouseleave="(event) => $emit('becomeUnhovered', event)"
      @click="(event) => {removeClass(section.crn); $emit('removeClass', event)}"
    >
      <div class="class-block-text">
        <h3>{{ course }}</h3>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .class-block {
    border-radius: 1em;
  }

  .class-block-outer {
    position: absolute;
  }

  .class-block-text {
    color: white;
  }

  .active {
    display: block;
    opacity: 92.5%;
    cursor: pointer;
  }

  .class-block-text {
    padding: .5em;
  }

  h3 {
    font-size: 1em;
    font-weight: 600;
    margin-top: 0em;
    margin-bottom: 0em;
  }

  h4 {
    font-size: .8em;
    font-weight: 400;
    margin-top: 0em;
  }
</style>