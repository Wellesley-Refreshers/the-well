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

  // constant, dummy results for all courses as Fuse results, when query == "".
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
  <div class="search-container">
    <div class="search-box-container">
      <input v-model="query" placeholder="Search for courses..." />
    </div>

    <div class="search-result-container">
      <Result
        v-for="courseResult in courseResults"
        :key="courseResult.item.crn"
        :crn="courseResult.item.crn"
        :score="courseResult.score"
      />
    </div>
  </div>
</template>

<style scoped>
  .search-container {
    --border-style: .25rem solid var(--main-color);

    border: .5rem solid var(--main-color);
    border-radius: 2rem;
    padding: 1em;

    width: 100%;
    height: 50rem;

    display: flex;
    flex-direction: column;
  }

  .search-box-container {
    display: flex;
    justify-content: space-between;
  }

  .search-result-container {
    overflow-y: auto;
  }

  input {
    background-color: var(--background-color-lighter);
    border: var(--border-style);
    border-radius: 3em;
    padding: .5em 1em;
    margin: .5em 0em;

    flex-grow: 2;
  }
</style>