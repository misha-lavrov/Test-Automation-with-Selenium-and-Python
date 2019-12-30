from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link2 = browser.find_element_by_link_text(formula)

    time.sleep(10)
    link2.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Misha")

    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Lavrov")

    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Vinnitsia")

    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraine")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(60)
    browser.quit()
