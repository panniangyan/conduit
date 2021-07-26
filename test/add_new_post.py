from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
)
assert user_name.text == "user2"
print(user_name.text)
time.sleep(1)
print(f"BEJELENTKEZÉS: {user_name}")


# NEW ARTICLE
new_article = browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
new_article.click()
time.sleep(5)

#input_post = ("test", "me", "blabablabal", "key")


article_title = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]/input')
article_about = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
article_text = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
article_tag = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/div/div/ul/li/input')

article_title.send_keys("title")
article_about.send_keys("me")
article_text.send_keys("blablabla")
article_tag.send_keys("key")

time.sleep(2)

publish_btn = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="app"]/div/div/div/div/form/button'))
    )
#        publish_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
publish_btn.click()
time.sleep(5)

published_title = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')
#assert(published_title.text == article_title.text)
print("New article published:", published_title.text)

browser.quit()
