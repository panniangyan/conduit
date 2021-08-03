from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib


browser = webdriver.Chrome("/usr/bin/chromedriver")
browser.get("http://localhost:1667")

browser.maximize_window()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()

browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
email = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
password = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
email.send_keys("user2@hotmail.com")
time.sleep(1)
password.send_keys("Userpass1")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
time.sleep(2)

user_name = WebDriverWait(
    browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@user2/"]'))
#    EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and text()="user2"]'))
)
assert user_name.text == "user2"
print(user_name.text)
time.sleep(1)
print(f"BEJELENTKEZÉS: {user_name.text}")


elements = browser.find_elements_by_class_name("article-preview")
title = browser.find_elements_by_xpath('//*[@class="article-preview"]/a/h1')

print(browser.find_element_by_xpath('//*[@class="nav-link router-link-exact-active active"]').text)
for j in title:
    print(j.text)

print(len(title))
print(title[0].text)

assert (browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text == title[0].text)

active_links = browser.find_elements_by_xpath('//*[@href="#/"]')

print("Test_4: DATA LISTING - active links on conduit homepage ", browser.current_url)
for k in active_links:
    print(k.text)
assert (browser.find_element_by_xpath('//*[@href="#/"]') == active_links[0])

browser.quit()



