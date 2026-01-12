<script setup>
  import allCourseSections from '../../../data/parsed/currentCourses.json';

  const props = defineProps({
    crn: Number,
    score: Number
  })

  const section = allCourseSections[props.crn];
</script>

<template>
  <div>
    <p>{{ `${section.dept} ${section.course_no}: ${section.title}` }}</p>
    <p>{{ props.score }}</p>
  </div>
</template>