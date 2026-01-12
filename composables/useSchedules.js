import { ref, computed } from "vue";
import allCourseSections from "../data/parsed/currentCourses.json";

const isInitialized = ref(false);

// Saved in local storage
const currentScheduleName = ref("");
const schedules = ref({});

const CURR_SCHEDULE_KEY = "currentSchedule";
const SCHEDULES_KEY = "schedules";

// Okabe-Ito
const palette = [
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

const initializeFromStorage = () => {
  if (import.meta.client && !isInitialized.value) {
    const currentScheduleSaved = localStorage.getItem(CURR_SCHEDULE_KEY);
    if (currentScheduleSaved !== null) {
      currentScheduleName.value = currentScheduleSaved;
    } else {
      currentScheduleName.value = "Schedule 1";
    }

    const schedulesSaved = localStorage.getItem(SCHEDULES_KEY);
    if (schedulesSaved !== null) {
      schedules.value = JSON.parse(schedulesSaved);
    } else {
      schedules.value = { "Schedule 1": [] };
    }

    isInitialized.value = true;

    // TODO: remove (testing)
    currentScheduleName.value = "Schedule 1";
    schedules.value = {
      "Schedule 1": {
        20803: "#555555",
        20001: "#ff7520",
        20912: "#444777",
        20018: "#7ddddd",
      },
    };
  }
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

// Initialize immediately when module is imported on client
if (import.meta.client) {
  initializeFromStorage();
}

// Kept for convenience
const currentSchedule = computed(
  () => schedules.value[currentScheduleName.value]
);
const currentSessions = computed(() => getAllSessions(currentSchedule.value));

export { schedules, currentSchedule, currentScheduleName, currentSessions };

export const makeNewSchedule = () => {
  // Get current number of schedules so we can automatically give
  // the new schedule the name "Schedule x"
  const currentScheduleNum = Object.keys(schedules.value).length;
  console.log(currentScheduleNum);

  const newScheduleName = `Schedule ${currentScheduleNum + 1}`;
  schedules.value[newScheduleName] = [];

  switchToSchedule(newScheduleName);

  saveSchedules();
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

  saveSchedules();
};

export const switchToSchedule = (scheduleName) => {
  currentScheduleName.value = scheduleName;
  saveCurrentSchedule();
};

export const addNewClass = (classCrn) => {
  const usedColors = Object.values(schedules.value[currentScheduleName.value]);

  const availableColors = palette.filter((color) => !(color in usedColors));

  const color =
    availableColors[Math.floor(Math.random() * availableColors.length)];

  schedules.value[currentScheduleName.value][classCrn] = color;
};

export const removeClass = (classCrn) => {
  delete schedules.value[currentScheduleName.value][classCrn];
  saveSchedules();
};
