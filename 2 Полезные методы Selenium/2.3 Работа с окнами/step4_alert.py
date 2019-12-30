from selenium import webdriver
import time
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".btn.btn-primary").click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    browser.find_element_by_css_selector(".btn.btn-primary").click()

    alert_text = browser.switch_to.alert.text
    answer = alert_text.split(": ")[-1]
    pyperclip.copy(answer)
finally:
    time.sleep(10)
    browser.quit()
