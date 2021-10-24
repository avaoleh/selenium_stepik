from selenium import webdriver
import time
import unittest


welcome_str = "Congratulations! You have successfully registered"
failed_str = "registration is failed"

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def link_test(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".first_block .form-control.first").send_keys("Ivan")
    browser.find_element_by_css_selector(".first_block .form-control.second").send_keys("Ivanov")
    browser.find_element_by_css_selector(".first_block .form-control.third").send_keys("email")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_test(link1),
                         welcome_str, failed_str)


    def test_reg2(self):
        self.assertEqual(link_test(link2),
                         welcome_str, failed_str)







if __name__ == "__main__":
    unittest.main()
