import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestAnswer:
    def test_is_basket_button_present(self, browser):
        browser.get(link)
        basket_button = browser.find_element_by_css_selector(".btn-add-to-basket").is_enabled()
        # basket_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
        assert basket_button, "button is missing"
        time.sleep(30)

        # 1. basket_button = browser.find_element_by_css_selector(".btn-a**-t*-b*****")
        # 2. basket_button = browser.find_elements_by_css_selector(".btn-a**-t*-b*****")
        # 3. basket_button = browser.find_element_by_class_name("btn-a**-t*-b*****")
        # 4. basket_button = browser.find_elements_by_class_name("btn-a**-t*-b*****")
