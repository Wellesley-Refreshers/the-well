<script setup>
  import Fuse from 'fuse.js';

  import Result from './pieces/Result.vue';

  import allCourseSections from "../../data/parsed/currentCourses.json";

  const query = ref("");
  const coursesSearchable = Object.values(allCourseSections).map((section) => {
    return {
      crn: section.crn,
      courseCode: `${section.dept} ${section.course_no} - ${section.section_no}`,
      title: section.title,
      professors: section.professors.join(" "),
      distributions: section.distributions.join(" "),
    }
  })

  const options = {
    includeScore: true,
    keys: [
      {
        name: "courseCode",
        weight: 100,
      },
      {
        name: "title",
        weight: 5,
      },
      {
        name: "professors",
        weight: 10,
      },
      {
        name: "distributions",
        weight: 8,
      }
    ]
  }

  const fuse = new Fuse(coursesSearchable, options);

  const courseResults = computed(() => fuse.search(query.value));
</script>

<template>
  <input v-model="query" placeholder="Search for courses..." />

  <div v-if="query != ''" class="search-results">
    <Result
      v-for="courseResult in courseResults"
      :crn="courseResult.item.crn"
      :score="courseResult.score"
      :key="courseResult.item.crn"
    />
  </div>
</template>

<style scoped>

</style>