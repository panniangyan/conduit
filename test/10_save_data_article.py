from selenium import webdriver
import time
import pprint
import csv
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/usr/bin/chromedriver")
browser.get("http://localhost:1667")
browser.maximize_window()

# # ACCEPT COOKIES
browser.find_element_by_xpath('//button[2]').click()

# # LOGIN
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
)
assert user_name.text == "user2"
print(user_name.text)
time.sleep(1)
print(f"BEJELENTKEZÉS: {user_name.text}")


### LIST DATA (user ARTICLES)

user_name = WebDriverWait(
            browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
)
user_name.click()







i =0
with open(f'{user_name.text}_article_list.csv', 'w') as out:
    dict_writer = csv.DictWriter(out, keys)
    dict_writer.writerows(extracted_data)
    i = i +1

time.sleep(2)
print("i", i)
