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

  // constant for all courses as Fuse results, when query == "".
  const allCourseResults = coursesSearchable.map((courseSearchable, index) => {
    return {
      item: courseSearchable,
      refIndex: index,
      score: 0,
    }
  })

  const options = {
    includeScore: true,
    keys: [
      {
        name: "courseCode",
        weight: 10,
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

  function search() {
    if (query.value === '') {
      return allCourseResults;
    } else {
      return fuse.search(query.value);
    }
  }

  const courseResults = computed(search);
</script>

<template>
  <input v-model="query" placeholder="Search for courses..." />

  <Result
    v-for="courseResult in courseResults"
    :crn="courseResult.item.crn"
    :score="courseResult.score"
    :key="courseResult.item.crn"
  />
</template>

<style scoped>

</style>