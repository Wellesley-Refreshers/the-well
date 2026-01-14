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
    <h4 class="section-title">{{ section.title }}</h4>
    <h6 class="section-professors">{{ section.professors.join(", ") }}</h6>
    <h5 class="section-sessions">{{ formatSessions(section).join("; ") }}</h5>
  </div>
</template>

<style scoped>
  .coursecode {
    margin: 0;
  }

  .section-no {
    font-weight: 400;
  }

  .section-title {
    font-weight: 600;
    margin: 0;
  }

  .section-professors {
    font-size: .8em;
    font-style: italic;
    margin: 0;
  }

  .section-sessions {
    margin-bottom: 0;
  }

  .result-container {
    border: var(--border-style);
    border-radius: 1.5em;
    margin: .8em 0em;
    padding: 1em;
  }

  .result-container:hover {
    background-color: var(--background-color-darker);
    cursor: pointer;
  }
</style>