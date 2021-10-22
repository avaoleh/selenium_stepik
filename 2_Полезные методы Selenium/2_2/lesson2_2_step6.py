import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)

    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id('answer').send_keys(x)

    option1 = browser.find_element_by_id('robotCheckbox').click()
    option2 = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector("button.btn").click()

    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
