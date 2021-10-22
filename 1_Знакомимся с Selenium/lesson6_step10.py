from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    #Case pre 1
    #       first_name = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    #     first_name.send_keys('reqired')
    #     last_name = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    #     last_name.send_keys('reqired')
    #     email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    #     email.send_keys('reqired')

    #Case pre 2
    # first_name = browser.find_element_by_class_name('first_block .form-group:nth-child(1) input.first')
    # first_name.send_keys('Ivan')
    #
    # second_name = browser.find_element_by_class_name('first_block .form-group:nth-child(2) input.second')
    # second_name.send_keys('Petrov')
    #
    # third_name = browser.find_element_by_class_name('first_block .form-group:nth-child(3) input.third')
    # third_name.send_keys('test@email.com')


    first_input = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    first_input.send_keys("Ivan")
    time.sleep(3)
    second_input = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    second_input.send_keys("Ivanov")
    time.sleep(3)
    third_input = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
    third_input.send_keys("ivan@ivan.com")
    time.sleep(3)


    #2 способ
    # labels = browser.find_elements_by_tag_name('label') # Список лэйблов над текстовыми полями
    # inputs = browser.find_elements_by_tag_name('input') # Список текстовых полей
    #
    # for i, label in enumerate(labels):          # Если последний символ
    #     if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
    #         inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!

    #3 способ
    # required_elements = browser.find_elements_by_css_selector('input[required]')
    # for element in required_elements:
    #     element.send_keys('required')

    #4 способ
    # xpath = "//label[contains(text(), '*')]/following-sibling::input"
    # input_list = browser.find_elements_by_xpath(xpath)
    # output_list = ['first_name', 'last_name', 'email']
    # # submit = browser.find_element_by_tag_name('button')
    #
    # for element, data in zip(input_list, output_list):
    #     element.send_keys(data)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
