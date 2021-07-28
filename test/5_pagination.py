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

extracted_data = []
count = 0
while True:
    time.sleep(2)
    rows = browser.find_elements_by_class_name("article-preview")
    time.sleep(2)
    current_page_number = int(browser.find_element_by_xpath('//*[@class="page-item active"]/a').text)
    print(f"Processing page {current_page_number}..")
    for i in rows:
        row = {}
        row["title"] = browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text
        row["text"] = browser.find_element_by_xpath('//*[@class="article-preview"]/a/p').text
        extracted_data.append(row)
        count = count + 1

    next_page_number = current_page_number + 1
    print(f"next page {next_page_number}, {current_page_number}..")
#    next_page_link = browser.find_element_by_xpath(f'//li[@data-test="page-link-{current_page_number + 1}"]/a')
    if current_page_number - 1 == next_page_number:
        next_page_link = browser.find_element_by_xpath(f'//li[@data-test="page-link-{next_page_number}"]/a')
        if NoSuchElementException:
            break
        else:
            next_page_link.click()

print(f"Exiting. Last page: {current_page_number}.")
print(count)
pprint.pp(extracted_data)
print(len(extracted_data))
