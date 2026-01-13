<script setup>
  import allCourseSections from '../../../data/parsed/currentCourses.json';
  import { addClass } from '../../../composables/useSchedules';

  const props = defineProps({
    crn: String,
    score: Number
  })

  const section = allCourseSections[props.crn];
</script>

<template>
  <div class="result-container" @click="addClass(props.crn)">
    <h3>{{ `${section.dept} ${section.course_no}` }} <span style="font-weight: 400">{{ section.section_no }}</span></h3>
    <h4>{{ section.title }}</h4>
  </div>
</template>

<style scoped>
  .result-container {
    border: 1px black solid;
  }

  .result-container:hover {
    background-color: gray;
    cursor: pointer;
  }
</style>