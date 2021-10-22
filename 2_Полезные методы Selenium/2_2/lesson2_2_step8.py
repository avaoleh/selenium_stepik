import time
import math
from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name('firstname').send_keys('Ivan')
    second_name = browser.find_element_by_name('lastname').send_keys('Petrov')
    third_name = browser.find_element_by_name('email').send_keys('test@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text_step8.txt')           # добавляем к этому пути имя файла
    file_upload = browser.find_element_by_id('file').send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
