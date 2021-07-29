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

accept_btn = browser.find_element_by_xpath('//button[contains (.,"I accept!")]')
print(accept_btn.text)
accept_btn.click()
time.sleep(2)
list_btn = browser.find_elements_by_xpath('//button')
assert(browser.find_elements_by_xpath('//button') == [])



print("cookies accepted", list_btn)

browser.quit()
