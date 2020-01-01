import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_parametrize_task(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    answer_field = browser.find_element_by_css_selector(".textarea.string-quiz__textarea.ember-text-area.ember-view")
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()
    answer = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    )
    answer_text = answer.text
    assert answer_text == "Correct!"



