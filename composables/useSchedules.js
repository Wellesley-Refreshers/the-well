import { ref, computed } from "vue";
import allCourseSections from "../data/parsed/currentCourses.json";

const isInitialized = ref(false);

// Saved in local storage
export const currentScheduleName = ref("");
export const schedules = ref({});
export const currentSchedule = computed(
  () => schedules.value[currentScheduleName.value]
);
export const currentSessions = computed(() =>
  getAllSessions(currentSchedule.value)
);

// Keys to save the above in local storage
const CURR_SCHEDULE_KEY = "currentSchedule";
const SCHEDULES_KEY = "schedules";

// Okabe-Ito
const PALETTE = [
  "#E69F00",
  "#56B4E9",
  "#009E73",
  "#F0E442",
  "#0072B2",
  "#D55E00",
  "#CC79A7",
];

function getMinutesSinceStartOfDay(day) {
  return 60 * day.getHours() + day.getMinutes();
}

function getRelativeMinutes(timeString) {
  let day = new Date(`1970-01-05T${timeString}`);
  return getMinutesSinceStartOfDay(day);
}

function selectRandomColor() {
  const usedColors = Object.values(schedules.value[currentScheduleName.value]);

  const availableColors = PALETTE.filter((color) => !(color in usedColors));

  return availableColors[Math.floor(Math.random() * availableColors.length)];
}

const getAllSessions = (schedule) => {
  let allSessions = [];

  for (const crn of Object.keys(schedule)) {
    const section = allCourseSections[crn];
    for (const meeting of section.meetings) {
      const meetingTime = meeting.meeting_time;
      allSessions.push({
        crn: crn,
        dayOfWeek: meetingTime.day_of_week,
        start: getRelativeMinutes(meetingTime.start),
        end: getRelativeMinutes(meetingTime.end),
      });
    }
  }

  return allSessions;
};

const saveSchedules = () => {
  if (import.meta.client) {
    const schedulesStringified = JSON.stringify(schedules.value);
    localStorage.setItem(SCHEDULES_KEY, schedulesStringified);
  }
};

const saveCurrentSchedule = () => {
  if (import.meta.client) {
    localStorage.setItem(CURR_SCHEDULE_KEY, currentScheduleName.value);
  }
};

const getDefaultScheduleName = () => {
  // Get current number of schedules so we can automatically give
  // the new schedule the name "Schedule x"
  const currentScheduleNum = Object.keys(schedules.value).length;
  return `Schedule ${currentScheduleNum + 1}`;
};

export const makeNewSchedule = () => {
  const newScheduleName = getDefaultScheduleName();
  schedules.value[newScheduleName] = {};

  saveSchedules();
  switchToSchedule(newScheduleName);
};

export const renameSchedule = (scheduleName, newName) => {
  if (newName in Object.keys(schedules.value)) {
    alert(`${newName} is already a schedule!`);
    return;
  }

  if (scheduleName in Object.keys(schedules.value)) {
    schedules.value[newName] = scheduleName.value[scheduleName];
    delete schedules.value[scheduleName];
  }

  saveSchedules();
};

export const removeSchedule = () => {
  if (Object.keys(schedules.value).length == 1) {
    alert("Cannot remove the last schedule!");
    return;
  }

  delete schedules.value[currentScheduleName.value];
  currentScheduleName.value = Object.keys(schedules.value)[0];

  saveCurrentSchedule();
  saveSchedules();
};

export const switchToSchedule = (scheduleName) => {
  currentScheduleName.value = scheduleName;
  saveCurrentSchedule();
};

export const addClass = (classCrn) => {
  if (Object.keys(currentSchedule.value).includes(classCrn)) {
    return;
  }

  const color = selectRandomColor();
  schedules.value[currentScheduleName.value][classCrn] = color;

  saveSchedules();
};

export const removeClass = (classCrn) => {
  // if (!(classCrn in Object.keys(currentSchedule))) {
  //   return;
  // }

  delete schedules.value[currentScheduleName.value][classCrn];
  saveSchedules();
};

const initializeFromStorage = () => {
  if (import.meta.client && !isInitialized.value) {
    const currentScheduleSaved = localStorage.getItem(CURR_SCHEDULE_KEY);
    const schedulesSaved = localStorage.getItem(SCHEDULES_KEY);

    if (currentScheduleSaved === null || schedulesSaved === null) {
      makeNewSchedule();
    } else {
      currentScheduleName.value = currentScheduleSaved;
      schedules.value = JSON.parse(schedulesSaved);
    }

    isInitialized.value = true;
  }
};

// Initialize immediately when module is imported on client
if (import.meta.client) {
  initializeFromStorage();
}

// export { schedules, currentSchedule, currentScheduleName, currentSessions };
