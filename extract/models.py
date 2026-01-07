from datetime import time
from enum import StrEnum

from pydantic import BaseModel, RootModel


class Model(BaseModel):
    pass


class DayOfWeek(StrEnum):
    MONDAY = "M"
    TUESDAY = "T"
    WEDNESDAY = "W"
    THURSDAY = "R"
    FRIDAY = "F"


class MeetingTime(Model):
    day_of_week: DayOfWeek
    start: time
    end: time


class Meeting(Model):
    meeting_time: MeetingTime
    location: str


class Course(BaseModel):
    crn: int
    dept: str
    course_no: str

    title: str
    description: str

    credit: float
    distributions: list[str]
    prerequisites: str


class CourseSection(Course):
    section_no: str

    professors: list[str]
    meetings: list[Meeting]

    crosslisted: str

    current_enrollment: int
    available_seats: int
    max_enrollment: int

    notes: str


CourseSections = RootModel[list[CourseSection]]
