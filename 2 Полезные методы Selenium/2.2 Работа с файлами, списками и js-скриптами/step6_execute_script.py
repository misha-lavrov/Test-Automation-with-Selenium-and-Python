from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
