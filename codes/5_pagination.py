from selenium import webdriver
import time
import pprint
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

# PAGINATION

page_list = browser.find_elements_by_class_name("page-link")
for page in page_list:
    page.click()
    print(page.text)


last_page = browser.find_element_by_xpath(f'//*[@class="page-item active" and @data-test="page-link-{page.text}"]')

print(last_page.text)
assert(page.text == last_page.text)

browser.quit()
