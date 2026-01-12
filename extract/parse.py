import json
import re
from datetime import datetime, time
from pathlib import Path
from typing import Any, Callable

from bs4 import BeautifulSoup
from models import CourseSection, Meeting, MeetingTime


def find(f: Callable, lst: list[Any]) -> Any | None:
    """
    Returns the first element of lst such that f is true. If no such element
    exists, returns None.

    Args:
        f (Callable): The function to try on each element.
        lst (list[Any]): The list to search through

    Returns:
        Any | None: The first element in lst for which f is true, or None if no such element exists.
    """
    for element in lst:
        if f(element):
            return element

    return None


class ParseException(Exception):
    """
    Exception for parsing errors.
    """

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def find_course_containers(soup: BeautifulSoup) -> list[BeautifulSoup]:
    """
    Given an HTML document, attempts to find all head elements.
    Assumes the given document is a proper Wellesley Course Browser site with
    all courses expanded.

    Args:
        soup (BeautifulSoup): The Course Browser HTML.

    Returns:
        list[BeautifulSoup]: A list of all the course-containing <div> elements.
    """
    return soup.select(".courseitem")


def parse_title(course_container: BeautifulSoup) -> str:
    """
    Given the course container, return the title of the course.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        str: The course title.
    """
    title_elements = course_container.select("div.coursename_big > p")

    if len(title_elements) != 1:
        raise ParseException(
            f"Expected to find 1 title element, but found {len(title_elements)}: {title_elements}"
        )

    return title_elements[0].text


def parse_course_code(course_container: BeautifulSoup) -> tuple[str, str, str]:
    """
    Given the course container, return the department abbreviation, course number,
    and section number.

    Args:
        course_container (BeautifulSoup): The course's containing <div>

    Returns:
        tuple[str, str, str]: (DEPT, course #, section #)
    """
    coursecode_elements = course_container.select("#divHeaders")

    if len(coursecode_elements) != 1:
        raise ParseException(
            f"Tried to parse the course code, but found {len(coursecode_elements)} elements: {course_container}"
        )

    coursecode = coursecode_elements[0].text
    return coursecode.strip().split()


def parse_professors(course_container: BeautifulSoup) -> list[str]:
    """
    Given the course container, return the professor(s).

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        list[str]: The professor(s) of that course.
    """
    professor_elements = course_container.select("a.professorname")
    return [professor_element.text for professor_element in professor_elements]


def parse_description(course_container: BeautifulSoup) -> str:
    """
    Given the course container, return the description of the course.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        str: The course's description.
    """
    desc_elements = course_container.select("div.coursedetail > div:first-child")

    if len(desc_elements) != 1:
        raise ParseException(
            f"Expected to find 1 description container, but found {len(desc_elements)}: {desc_elements}"
        )

    return desc_elements[0].text


def parse_enrollment_data(course_container: BeautifulSoup) -> tuple[int, float, int, int, int]:
    """
    Given the course container of a course in the Course Browser, return
    (CRN, credit, curr_enrollment, available_seats, max_enrollment)

    Args:
        head_element (BeautifulSoup): The course's containing <div>.

    Returns:
        tuple[int, float, int, int, int]: (CRN, credit, curr_enrollment, available_seats, max_enrollment)
    """
    course_detail_elements = course_container.select(".coursedetail01")
    enrollment_element = course_detail_elements[0]

    regex = r"CRN: (\d+); Credit Hours: (\d+\.?\d*); Current Enrollment: (\d+); Seats Available: (\d+); Max Enrollment: (\d+);"

    match = re.match(regex, enrollment_element.text)
    d = match.groups()

    return int(d[0]), float(d[1]), int(d[2]), int(d[3]), int(d[4])


def parse_meetings(course_container: BeautifulSoup) -> list[Meeting]:
    """
    Given the course container of a course in the Course Browser, return
    a list of the weekly meeting times.

    Args:
        course_container (BeautifulSoup): The course's containing <div>

    Returns:
        list[Meeting]: The course section's meeting times.
    """
    meeting_element = course_container.select(".coursedetail01")[1]

    def parse_meeting_times(meeting_time_str: str) -> list[MeetingTime]:
        """
        Helper function to parse a list of meeting times from a string.
        The string should be of the form:

            "Meeting Time(s): TF - 12:45 PM - 2:00 PM Loc:"

        Whitespace and semicologns before or after the string will be ignored.

        Args:
            meeting_time_str (str): The meeting time string.

        Returns:
            list[MeetingTime]: A list of meeting times specified by the string.
        """
        meeting_time_str = meeting_time_str.strip(" ;\n\t\r")

        day_of_week_regex = r"[MTWRF]+"
        time_regex = r"\d+:\d+ [AP]M"
        regex = rf"({day_of_week_regex}) - ({time_regex}) - ({time_regex})"

        match = re.search(regex, meeting_time_str)

        def get_time(time_match) -> time:
            time_format = "%I:%M %p"
            return datetime.strptime(time_match, time_format).time()

        start, end = get_time(match.group(2)), get_time(match.group(3))

        days_of_week = match.group(1)

        return [
            MeetingTime(day_of_week=day_of_week, start=start, end=end)
            for day_of_week in days_of_week
        ]

    def parse_location(location_element: BeautifulSoup) -> str:
        """
        Helper function to parse a location element. Expects it to be held in
        an <a> tag. Raises a ParseException if not.

        Args:
            location_element (BeautifulSoup): The element containing the location.

        Returns:
            str: The location.

        Raises:
            ParseException: if the location element is not an <a> tag.
        """
        if location_element.name != "a":
            raise ParseException(
                f"Expected location element to be an <a> tag, but was actually {location_element.name}!"
            )

        return location_element.text

    # We need to manually scan the contents array.
    # It should go (str w/ meeting times, loc, str w/ meeting times, loc, ...)
    contents = meeting_element.contents

    all_class_meetings = []

    time_content_index = 0
    location_content_index = 1
    while location_content_index < len(contents):
        time_content = contents[time_content_index]
        loc_content = contents[location_content_index]

        meeting_times = parse_meeting_times(time_content)
        location = parse_location(loc_content)

        meetings = [
            Meeting(meeting_time=meeting_time, location=location) for meeting_time in meeting_times
        ]
        all_class_meetings.extend(meetings)

        # REMINDER: we're scanning the list in pairs.
        # TODO: could be done more pythonically by reshaping the list first.
        time_content_index += 2
        location_content_index += 2

    return all_class_meetings


def parse_distributions(course_container: BeautifulSoup) -> list[str]:
    """
    Given a course container, returns the distributions as a list.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        list[str]: The distributions for the course.
    """
    coursedetail_elements = course_container.select(".coursedetail01")

    def is_distributions(soup: BeautifulSoup) -> bool:
        return "Distributions: " in soup.text

    distributions_element = find(is_distributions, coursedetail_elements)

    if distributions_element is None:
        return []

    regex = r"([A-Z]+) - \w*[;\s]"
    return re.findall(regex, distributions_element.text)


def parse_prerequisites(course_container: BeautifulSoup) -> str:
    """
    Given a course container, return prerequisites as a string.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        str: The prerequisites.
    """
    coursedetail_elements = course_container.select(".coursedetail01")

    def is_prerequisites(soup: BeautifulSoup) -> bool:
        return "Prerequisites(s): " in soup.text

    prerequisites_element = find(is_prerequisites, coursedetail_elements)

    if prerequisites_element is None:
        return ""

    regex = r"Prerequisites\(s\): (.*)"
    return re.search(regex, prerequisites_element.text).group(1)


def parse_crosslisted(course_container: BeautifulSoup) -> str:
    """
    Given a course container, returns any crosslisted classes.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        str: Description of the crosslisted course(s).
    """
    coursedetail_elements = course_container.select(".coursedetail01")

    def is_crosslisted(soup: BeautifulSoup) -> bool:
        return "Cross-listed courses: " in soup.text

    crosslisted_element = find(is_crosslisted, coursedetail_elements)

    if crosslisted_element is None:
        return ""

    regex = r"Cross-listed courses: (.*)"
    return re.search(regex, crosslisted_element.text).group(1)


def parse_notes(course_container: BeautifulSoup) -> str:
    """
    Given a course container, return any notes on that course.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        str: Notes on the course.
    """
    coursedetail_elements = course_container.select(".coursedetail01")

    def is_notes(soup: BeautifulSoup) -> bool:
        return "Notes: " in soup.text

    notes_element = find(is_notes, coursedetail_elements)

    if notes_element is None:
        return ""

    regex = r"Notes: (.*)"
    return re.search(regex, notes_element.text).group(1)


def parse_course_section(course_container: BeautifulSoup) -> CourseSection:
    """
    Given a course container, returns its corresponding CourseSection object.

    Args:
        course_container (BeautifulSoup): The course's containing <div>.

    Returns:
        CourseSection: The course represented as a CourseSection object.
    """
    dept, course_no, section_no = parse_course_code(course_container)
    crn, credit, curr_enroll, available_seats, max_enroll = parse_enrollment_data(course_container)

    return CourseSection(
        crn=crn,
        dept=dept,
        course_no=course_no,
        section_no=section_no,
        title=parse_title(course_container),
        description=parse_description(course_container),
        professors=parse_professors(course_container),
        meetings=parse_meetings(course_container),
        credit=credit,
        distributions=parse_distributions(course_container),
        prerequisites=parse_prerequisites(course_container),
        current_enrollment=curr_enroll,
        available_seats=available_seats,
        max_enrollment=max_enroll,
        crosslisted=parse_crosslisted(course_container),
        notes=parse_notes(course_container),
    )


def parse_course_browser(course_browser_dom: BeautifulSoup) -> list[CourseSection]:
    """
    Given a course browser as a BeautifulSoup, returns a list of CourseSection
    objects describing the course browser.

    Args:
        course_browser_dom (BeautifulSoup): The DOM of the Course Browser as a BeautifulSoup

    Returns:
        list[CourseSection]: The Course Browser as a list of CourseSection objects.
    """
    course_containers = find_course_containers(course_browser_dom)

    return [parse_course_section(course_container) for course_container in course_containers]


def main() -> None:
    semester = "sp26"

    IN_FP = Path.cwd() / "data" / "raw" / f"{semester}.html"
    OUT_FP = Path.cwd() / "data" / "parsed" / f"{semester}.json"
    PERMANENT_FP = Path.cwd() / "data" / "parsed" / "currentCourses.json"

    with IN_FP.open() as file:
        course_browser_dom = BeautifulSoup(file, features="lxml")

    course_sections = parse_course_browser(course_browser_dom)

    course_sections_by_crn = {
        course_section.crn: course_section.model_dump() for course_section in course_sections
    }

    def default_serializer(to_serialize: Any):
        if isinstance(to_serialize, time):
            return to_serialize.strftime("%H:%M:%S")

    with OUT_FP.open("w") as out_file:
        json.dump(course_sections_by_crn, out_file, default=default_serializer)

    PERMANENT_FP.symlink_to(OUT_FP)


if __name__ == "__main__":
    main()
