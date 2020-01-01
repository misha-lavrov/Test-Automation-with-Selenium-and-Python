from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_items(browser):
    button = None
    try:
        browser.get(link)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
        )
    finally:
        assert button is not None, "There is no such button"

