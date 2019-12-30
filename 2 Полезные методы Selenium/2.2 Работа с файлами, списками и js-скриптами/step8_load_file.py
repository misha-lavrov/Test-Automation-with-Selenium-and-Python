from selenium import webdriver
import os
import time
import pyperclip

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys("Misha")
    browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys("Lavrov")
    browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys("misha.lavrov1999@gmail.com")

    file_input = browser.find_element_by_css_selector('[type=file]')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_input.send_keys(file_path)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

    #copy answer text to clipboard (for very lazy guys)
    alert_text = browser.switch_to.alert.text
    answer = alert_text.split(": ")[-1]
    pyperclip.copy(answer)

finally:
    time.sleep(10)
    browser.quit()