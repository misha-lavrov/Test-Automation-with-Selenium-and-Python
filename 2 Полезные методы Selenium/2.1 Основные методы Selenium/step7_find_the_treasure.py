from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_css_selector("#treasure")
    x = picture.get_attribute("valuex")

    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
