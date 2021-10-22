# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import os
import math
import time

link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element_by_id("button")

# except Exception as error:
#     print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
