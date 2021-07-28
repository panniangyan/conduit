from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


browser = webdriver.Chrome("/usr/bin/chromedriver")
browser.get("http://localhost:1667")

browser.maximize_window()
browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()

browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
email = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
email.send_keys("user2@hotmail.com")
time.sleep(1)
password.send_keys("Userpass1")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(1)
user_name = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a'))
#    EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and text()="user2"]'))
)
assert user_name.text == "user2"
print(user_name.text)
time.sleep(1)
print(f"BEJELENTKEZÉS: {user_name.text}")


### LOGOUT

logout_btn = browser.find_element_by_xpath('//*[@class="nav-link" and contains(text(),"Log out")]')
assert(logout_btn.text == ' Log out')
print("Find logout button:", logout_btn.text)
time.sleep(2)
logout_btn.click()
sign_in_btn = browser.find_element_by_xpath('//*[@href="#/login"]')
assert(sign_in_btn.text == 'Sign in')
print("Back to homepage:", sign_in_btn.text)
time.sleep(2)
print("LOGGED OUT")


browser.quit()