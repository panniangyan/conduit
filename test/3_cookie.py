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
time.sleep(2)

print("cookies accepted")
