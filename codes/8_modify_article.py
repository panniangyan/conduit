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

# modify post
title_list = []
#user = browser.find_element_by_xpath('//*[@class="nav-link" and text()="user2"]')
user_name.click()
time.sleep(2)
old_title = browser.find_element_by_xpath('//*[@class="preview-link"]/h1')
title_list.append(old_title.text)
old_title.click()
#################################################################################
# edit article btn
time.sleep(2)
edit_article_btn = browser.find_element_by_xpath('//*[@class="article-meta"]/span/a').click()
time.sleep(2)
#edit_article_btn = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/span/a/span').click()
new_title = "OhLALA"
title_list.append(new_title)
change_title = WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@placeholder="Article Title"]'))
)
change_title.clear()
change_title.send_keys(new_title)
time.sleep(2)
submit_btn = browser.find_element_by_xpath('//button[@type="submit"]')
submit_btn.click()
time.sleep(2)
print(title_list)

new_post_title = WebDriverWait(
    browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@class="container"]/h1'))
)
title_list.append(new_post_title.text)
time.sleep(2)
assert(new_post_title.text == new_title)
time.sleep(2)
print(f"ADATMÓDOSITÁS: blog cim átirása {title_list[0]} -> {title_list[2]} ")
#print(f"-> {new_post_title.text}")
#print(f"{new_title}")

print(title_list)

browser.quit()
