from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    # 1
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute("valuex")
    y = str(math.log(abs(12*math.sin(int(x)))))

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()

    # elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
    #
    # for elem in elements_to_select:
    #     browser.find_element_by_css_selector(elem).click()

    time.sleep(10)


#------------------------------  1 ----------------------------
# Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
# valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

# Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
# browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))

# Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
# for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
#   browser.find_element_by_css_selector(selector).click()

#------------------------------  2 ----------------------------
