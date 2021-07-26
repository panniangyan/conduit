import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome("/usr/bin/chromedriver")
browser.get("http://localhost:1667")




assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."

    # # Test3 ACCEPT COOKIES
#    def test__accept_cookies(self):

browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
time.sleep(2)

    # # Test4 REGISTRATION

browser.maximize_window()
browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
username = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
email = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
password = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[3]/input')

username.send_keys("user1")
email.send_keys("user1@hotmail.com")
password.send_keys("Userpass1")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(2)
        # testing popup window:
#ref_text = "Registration failed!"
#ref_text = "Welcome"
welcome = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
    )
print(welcome.text)
#assert (welcome.text == ref_text)
#        print(alert.text)
#        self.browser.switch_to.alert()
#        assert self.browser.find_element_by_xpath('/html/body/div[2]/div/div[2]').text == ref_text
                #(/html/body/div[2]/div/div[3]).text == "Email already taken."
#        self.browser.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button').click()
# ref_text '/html/body/div[2]/div/div[2]' Welcome

time.sleep(2)
