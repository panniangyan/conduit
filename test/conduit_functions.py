import time
from csv import reader

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# # # # # # # # # # # # # # # # # # # # # # # # defining functions # # # # # # # # # # # # # # # # # # # # # # # # 


def xpath(browser, xpath_search):
    return browser.find_element_by_xpath(xpath_search)


def homepage(browser):
    time.sleep(2)
    print(f"conduit HOMEPAGE loaded", {browser.current_url})


def accept_cookies(browser):
    browser.find_element_by_xpath('//button[contains (.,"I accept!")]').click()
    time.sleep(2)


def conduit_login(browser, user_login):
    xpath(browser, '//*[@href="#/login"]').click()
    time.sleep(1)
    for k, v in user_login.items():
        xpath(browser, f'//*[@placeholder="{k}"]').send_keys(v)
    time.sleep(1)
    xpath(browser, '//button[1]').click()
    time.sleep(1)


def add_new_article(browser, input_post):
    article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]
    browser.find_element_by_xpath('//*[@href="#/editor"]').click()
    time.sleep(2)
    fill_article = []
    i = 0
    while i < len(input_post):
        fill = browser.find_element_by_xpath(f'//*[@placeholder="{article_data[i]}"]').send_keys(input_post[i])
        fill_article.append(fill)
        i = i + 1
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()

