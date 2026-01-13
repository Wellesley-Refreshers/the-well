<script setup>
  import allCourseSections from '../../../data/parsed/currentCourses.json';
  import { addClass } from '../../../composables/useSchedules';

  const props = defineProps({
    crn: String,
    score: Number
  })

  function formatTime(timeStr) {
    let time = new Date(`1970-01-05T${timeStr}`);
    return time.toLocaleTimeString();
  }

  function formatSessions(section) {
    let sessionsFormatted = [];
    for (const session of section.sessions) {
      const daysOfWeekFormatted = session.meeting_time.days_of_week.join("");
      const start = session.meeting_time.start;
      const end = session.meeting_time.end;
      sessionsFormatted.push(`${daysOfWeekFormatted} ${formatTime(start)} - ${formatTime(end)}`);
    }
    return sessionsFormatted;
  }

  const section = allCourseSections[props.crn];
</script>

<template>
  <div class="result-container" @click="addClass(props.crn)">
    <h3 class="coursecode">{{ `${section.dept} ${section.course_no}` }} <span class="section-no">{{ section.section_no }}</span></h3>
    <h4>{{ section.title }}</h4>
    <h5>{{ formatSessions(section).join("; ") }}</h5>
  </div>
</template>

<style scoped>
  .result-container {
    border: 1px black solid;
  }

  .result-container:hover {
    background-color: rgb(229, 229, 229);
    cursor: pointer;
  }

  .section-no {
    font-weight: 400;
  }
</style>