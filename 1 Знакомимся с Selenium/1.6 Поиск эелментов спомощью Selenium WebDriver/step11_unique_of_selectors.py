from selenium import webdriver
import time

# choose one of the links and comments the other

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # fill the required fields

    input1 = browser.find_element_by_css_selector(".first_block [class=\"form-control first\"]")
    input1.send_keys("Misha")

    input2 = browser.find_element_by_css_selector(".first_block [class=\"form-control second\"]")
    input2.send_keys("Lavrov")

    input3 = browser.find_element_by_css_selector(".first_block [class=\"form-control third\"]")
    input3.send_keys("m.l@gmail.com")

    time.sleep(1)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()