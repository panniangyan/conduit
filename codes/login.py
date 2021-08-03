import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Conduit(object):
    def setup(self):
        self.browser = webdriver.Chrome("/usr/bin/chromedriver")
        self.browser.get("http://localhost:1667")

    def teardown(self):
        self.browser.quit()

    # # Test0 HOMEPAGE
    def home_page(self):
        time.sleep(2)
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."

    # # Test3 ACCEPT COOKIES
    def accept_cookies(self):
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
        time.sleep(2)

    # Test2 LOGIN user2
    def navigate_to_login(self):
        self.browser.maximize_window()
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        email = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')

        email.send_keys("user2@hotmail.com")
        time.sleep(2)
        password.send_keys("Userpass1")
        time.sleep(2)

        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(2)
        element = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a')
        time.sleep(2)
        print(element.text)
        assert element.text == "user2"



