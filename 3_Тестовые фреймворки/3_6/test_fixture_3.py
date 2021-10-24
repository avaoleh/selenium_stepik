import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

message_str = ""

@pytest.fixture(scope='function')
def answer():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # ожидание прогрузки страницы
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    print(message_str)
    browser.quit()

@pytest.mark.parametrize('link', links)
class TestAnswer:
    def test_guest_should_see_message(self, browser, link, answer):
        global message_str
        browser.get(link)
        browser.find_element_by_tag_name("textarea").send_keys(answer)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        txt_answer = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))).text

        if txt_answer != "Correct!":
            message_str = message_str + txt_answer

        assert txt_answer == 'Correct!', 'message is not "Correct!"'
