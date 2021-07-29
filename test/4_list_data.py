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


### LIST DATA (user ARTICLES)

user_name = WebDriverWait(
            browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
).click()


extracted_data = []
count = 0

time.sleep(2)
row = {}
rows = browser.find_elements_by_class_name("article-preview")
print(len(rows))

#print(rows)
time.sleep(2)
while count < len(rows):
    row["count"]["id"] = count
    row["count"]["title"] = browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text
    row["count"]["user"] = browser.find_element_by_xpath('//*[@class="info"]/a').text
    row["count"]["date"] = browser.find_element_by_class_name("date").text
    row["count"]["text"] = browser.find_element_by_xpath('//*[@class="article-preview"]/a/p').text
    row["count"]["tag"] = browser.find_element_by_xpath('//*[@class="tag-list"]/a').text
    extracted_data.append(row)
    count = count + 1
    print(row["count"]["id"], row["count"]["title"], row["count"]["date"], row["count"]["user"], )

for i in rows:
    print(browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text)


print(count)
print(extracted_data)
print(len(extracted_data))

time.sleep(2)

browser.quit()
