import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome("/usr/bin/chromedriver")
browser.get("http://localhost:1667")
browser.maximize_window()

assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
assert browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."

    # # Test3 ACCEPT COOKIES
#    def test__accept_cookies(self):

browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
time.sleep(2)

    # # Test4 REGISTRATION
user_input = {"name": "test5",
              "email": "USeR5@hotmail.com",
              "password": "Userpass1"
              }

browser.find_element_by_xpath('//*[@href="#/register"]').click()
username = browser.find_element_by_xpath('//*[@placeholder="Username"]')
email = browser.find_element_by_xpath('//*[@placeholder="Email"]')
password = browser.find_element_by_xpath('//*[@placeholder="Password"]')

username.send_keys(user_input["name"])
email.send_keys(user_input["email"])
password.send_keys(user_input["password"])
time.sleep(2)
browser.find_element_by_xpath('//button[1]').click()
time.sleep(2)
        # testing popup window:
ref_text_fail = "Registration failed!"
ref_text_success = "Welcome!"
welcome = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
    )
if welcome.text == ref_text_success:
    print(welcome.text)
    print(browser.find_element_by_css_selector(".swal-text").text)
elif welcome.text == ref_text_fail:
    print(welcome.text)
    print(browser.find_element_by_css_selector(".swal-text").text)
assert (welcome.text == ref_text_fail)

browser.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
time.sleep(2)
