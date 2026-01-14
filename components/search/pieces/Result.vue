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

  function formatSession(session) {
    const daysOfWeekFormatted = session.meeting_time.days_of_week.join("");
    const start = session.meeting_time.start;
    const end = session.meeting_time.end;

    return `${daysOfWeekFormatted} ${formatTime(start)} - ${formatTime(end)}`;
  }

  const section = allCourseSections[props.crn];
</script>

<template>
  <div class="result-container" @click="addClass(props.crn)">
    <h3 class="coursecode">{{ `${section.dept} ${section.course_no}` }} <span class="section-no">{{ section.section_no }}</span></h3>
    <h4 class="section-title">{{ section.title }}</h4>
    <h6 class="section-professors">{{ section.professors.join(", ") }}</h6>

    <div class="section-sessions">
      <span v-for="session of section.sessions" class="section-session">{{ formatSession(session) }}</span>
    </div>
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
    margin-bottom: 1em;
  }

  .section-sessions {
    display: flex;
    gap: .5rem;
    margin-bottom: 0;
  }

  .section-session {
    padding: .25em .5em;
    border-radius: 1em;
    background-color: var(--secondary-color);
  }

  .result-container {
    border: var(--border-style);
    border-radius: 1.5em;
    margin: .8em 0em;
    padding: 1em;

    background-color: var(--main-color);
    color: white;
  }

  .result-container:hover {
    opacity: 95%;
    cursor: pointer;
  }
</style>