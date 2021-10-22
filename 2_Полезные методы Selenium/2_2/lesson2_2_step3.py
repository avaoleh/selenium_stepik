import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #number1 = int(browser.find_element_by_id("num1").text)
    #number2 = int(browser.find_element_by_id("num2").text)
    sum = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    #sum = str(number1 + number2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element_by_tag_name(".btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
