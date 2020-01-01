import unittest
from selenium import webdriver
import time


class TestRegistrationPage(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

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

        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test failed!")


    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

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

        browser.quit()

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Test failed!")


if __name__ == "__main__":
    unittest.main()

