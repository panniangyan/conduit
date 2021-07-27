from selenium import webdriver
import time
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


# NEW ARTICLE

new_article = browser.find_element_by_xpath('//*[@href="#/editor"]')
new_article.click()
time.sleep(2)

input_post = ["test", "me", "blabablabal", "key"]
article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]
#print(f"{input_post[0]}, placeholder=\"{article_data[1]}\", {len(article_data)}")

fill_article = []
i = 0
while i < 3:
    fill = browser.find_element_by_xpath(f'//*[@placeholder="{article_data[i]}"]').send_keys(input_post[i])
    fill_article.append(fill)
    print(fill_article[i], i, input_post[i])
    i = i + 1

publish_btn = WebDriverWait(
    browser, 5).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//button[1]'))
    ).click()
time.sleep(2)

# assert
published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
assert(published_title.text == input_post[0])
print("New article published:", published_title.text)

browser.quit()
