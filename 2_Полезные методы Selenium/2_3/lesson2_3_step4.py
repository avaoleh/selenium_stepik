# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import os
import math
import time

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name(".btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = int(browser.find_element_by_id("input_value").text)
    x = calc(x_element)

    input_answer = browser.find_element_by_id("answer").send_keys(x)
    submit = browser.find_element_by_tag_name(".btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
