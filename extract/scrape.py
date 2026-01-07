from pathlib import Path
from time import sleep
from typing import Callable

from selenium import webdriver
from selenium.webdriver.common.by import By

COURSE_BROWSER = "https://courses.wellesley.edu"
COURSE_SELECTOR = "#course_listing > section > div > a"
OUTPUT_FILE = Path("./data/raw/sp26.html")


def retry_until_success(f: Callable) -> None:
    success = False
    while not success:
        try:
            f()
            success = True
        except Exception as e:
            print(e)


def main() -> None:
    with webdriver.Chrome() as driver:
        driver = webdriver.Chrome()
        driver.get(COURSE_BROWSER)

        elements = driver.find_elements(By.CSS_SELECTOR, value=COURSE_SELECTOR)
        for element in elements:
            element.click()
            sleep(0.5)

        with OUTPUT_FILE.open("w") as file:
            file.write(driver.page_source)


if __name__ == "__main__":
    main()
