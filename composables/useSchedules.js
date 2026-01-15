import { ref, computed } from "vue";
import allCourseSections from "../data/parsed/currentCourses.json";

const isInitialized = ref(false);

// Saved in local storage
export const currentScheduleIndex = ref(0);
export const schedules = ref([]);
const currentSchedule = computed(
  () => schedules.value[currentScheduleIndex.value]
);
export const currentScheduleName = computed(() => currentSchedule.value.name);
export const currentCrnColors = computed(() => currentSchedule.value.crnColors);
export const currentSessions = computed(() =>
  getAllSessions(currentCrnColors.value)
);

// Keys to save the above in local storage
const CURR_SCHEDULE_KEY = "currentScheduleIndex";
const SCHEDULES_KEY = "schedules";

// Okabe-Ito
const PALETTE = [
  "#E69F00",
  "#56B4E9",
  "#009E73",
  "#c1b734ff",
  "#0072B2",
  "#D55E00",
  "#CC79A7",
];

//
// HELPERS
//

function getMinutesSinceStartOfDay(day) {
  return 60 * day.getHours() + day.getMinutes();
}

function getRelativeMinutes(timeString) {
  let day = new Date(`1970-01-05T${timeString}`);
  return getMinutesSinceStartOfDay(day);
}

function selectRandomColor() {
  const usedColors = Object.values(currentCrnColors.value);

  const availableColors = PALETTE.filter(
    (color) => !usedColors.includes(color)
  );

  return availableColors[Math.floor(Math.random() * availableColors.length)];
}

function getDefaultScheduleName() {
  // Get current number of schedules so we can automatically give
  // the new schedule the name "Schedule x"
  const currentScheduleNum = Object.keys(schedules.value).length;
  return `Schedule ${currentScheduleNum + 1}`;
}

const getAllSessions = (crnColors) => {
  let allSessions = [];

  for (const crn of Object.keys(crnColors)) {
    const section = allCourseSections[crn];
    for (const session of section.sessions) {
      const meetingTime = session.meeting_time;
      for (const dayOfWeek of meetingTime.days_of_week) {
        allSessions.push({
          crn: crn,
          dayOfWeek: dayOfWeek,
          start: getRelativeMinutes(meetingTime.start),
          end: getRelativeMinutes(meetingTime.end),
        });
      }
    }
  }

  return allSessions;
};

//
// SAVING
//

const saveSchedules = () => {
  if (import.meta.client) {
    const schedulesStringified = JSON.stringify(schedules.value);
    localStorage.setItem(SCHEDULES_KEY, schedulesStringified);
  }
};

const saveCurrentScheduleIndex = () => {
  if (import.meta.client) {
    localStorage.setItem(CURR_SCHEDULE_KEY, currentScheduleIndex.value);
  }
};

//
// SCHEDULES
//

export const makeNewSchedule = () => {
  schedules.value.push({
    name: getDefaultScheduleName(),
    crnColors: {},
  });

  saveSchedules();
  switchToSchedule(schedules.value.length - 1);
};

export const renameSchedule = (newName) => {
  currentSchedule.value.name = newName;

  saveSchedules();
};

export const removeSchedule = () => {
  if (Object.keys(schedules.value).length == 1) {
    alert("Cannot remove the last schedule!");
    return;
  }

  schedules.value.splice(currentScheduleIndex.value, 1);

  if (currentScheduleIndex.value > 0) {
    currentScheduleIndex.value -= 1;
  }

  saveCurrentScheduleIndex();
  saveSchedules();
};

export const switchToSchedule = (scheduleIndex) => {
  currentScheduleIndex.value = scheduleIndex;
  saveCurrentScheduleIndex();
};

//
// CLASSES
//

export const addClass = (classCrn) => {
  if (Object.keys(currentCrnColors.value).includes(classCrn)) {
    return;
  }

  const color = selectRandomColor();
  currentCrnColors.value[classCrn] = color;

  saveSchedules();
};

export const removeClass = (classCrn) => {
  // if (!(classCrn in Object.keys(currentSchedule))) {
  //   return;
  // }

  delete currentCrnColors.value[classCrn];
  saveSchedules();
};

//
// MAIN
//

const initializeFromStorage = () => {
  if (import.meta.client && !isInitialized.value) {
    const currentScheduleSaved = localStorage.getItem(CURR_SCHEDULE_KEY);
    const schedulesSaved = localStorage.getItem(SCHEDULES_KEY);

    if (currentScheduleSaved === null || schedulesSaved === null) {
      makeNewSchedule();
    } else {
      currentScheduleIndex.value = currentScheduleSaved;
      schedules.value = JSON.parse(schedulesSaved);
    }

    isInitialized.value = true;
  }
};

initializeFromStorage();
