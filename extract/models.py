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
    days_of_week: list[DayOfWeek]
    start: time
    end: time


class Session(Model):
    meeting_time: MeetingTime
    location: str


class Course(BaseModel):
    dept: str
    course_no: str

    title: str
    description: str

    credit: float
    distributions: list[str]
    prerequisites: str


class CourseSection(Course):
    crn: str
    section_no: str

    professors: list[str]
    sessions: list[Session]

    crosslisted: str

    current_enrollment: int
    available_seats: int
    max_enrollment: int

    notes: str


CourseSections = RootModel[list[CourseSection]]
