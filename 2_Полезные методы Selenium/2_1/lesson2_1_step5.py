from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    # 1
    browser.get(link)
    # 2-4
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id ("answer")
    input1.send_keys(str(y))
    # 5
    ch1 = browser.find_element_by_id ("robotCheckbox")
    ch1.click()
    # 6
    r1 = browser.find_element_by_id ("robotsRule")
    r1.click()
    # 7
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    time.sleep(10)


#------------------------------  1 ----------------------------
# try:
#     browser.get(link)
#     x1 = browser.find_element_by_css_selector('#input_value').text
#     y = calc(x1)
#     browser.find_element_by_css_selector('#answer').send_keys(y)
#     browser.find_element_by_css_selector('#robotCheckbox').click()
#     browser.find_element_by_css_selector('#robotsRule').click()
#     browser.find_element_by_css_selector('button[type="submit"]').click()
#     answer = browser.switch_to.alert.text
#     print(answer.split()[-1])
# finally:
#     time.sleep(10)
#     browser.quit()

#------------------------------  2 ----------------------------
# def print_answer(remote: webdriver.Remote):
#     alert = remote.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/math.html"
# browser.get(link)
#
# try:
#     x_element = browser.find_element_by_id("input_value").text
#     browser.find_element_by_id("answer").send_keys(calc(x_element))
#     elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
#
#     for elem in elements_to_select:
#         browser.find_element_by_css_selector(elem).click()
