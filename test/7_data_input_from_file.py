from selenium import webdriver
import time
import csv
from csv import reader
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




### DATA INPUT FROM FILE
#input_post = ["Hello", "me", "oooooooooooooooooooooooobbbbbbbbbbbbbbbbbb", "key2"]
#article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

with open('input_article.csv', 'r') as data:
    csv_reader = reader(data)
    # Get all rows of csv from csv_reader object as list of tuples
    input_post = list(map(tuple, csv_reader))
        # display all rows of csv
    #print(input_post)

#print(input_post)
#print(input_post[0])
#print(input_post[1])
#print(input_post[2])

# NEW ARTICLE

new_article = browser.find_element_by_xpath('//*[@href="#/editor"]')
#new_article.click()
time.sleep(2)

#print(f"{input_post[0]}, placeholder=\"{article_data[1]}\", {len(article_data)}")
#input_post = ["Hello", "me", "oooooooooooooooooooooooobbbbbbbbbbbbbbbbbb", "key2"]
#article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

fill_article = []
#i = 0
#j = 0
post_num = len(input_post) - 1
line_num = len(input_post[0]) - 1
#print(line_num, post_num)
#print(4, input_post[4][0], input_post[4][1], input_post[4][2], input_post[4][3])

for i in range(1, post_num):
    browser.find_element_by_xpath('//*[@href="#/editor"]').click()
    print(i, input_post[i][0], input_post[i][1], input_post[i][2], input_post[i][3])
    time.sleep(2)
    for j in range(0, line_num):
        fill = browser.find_element_by_xpath(f'//*[@placeholder="{input_post[0][j]}"]').send_keys(input_post[i][j])
        fill_article.append(fill)
    #print(i, input_post[i][0], input_post[i][1], input_post[i][2], input_post[i][3])
    time.sleep(2)
    publish_btn = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
   # publish_btn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
    time.sleep(2)


#    print(i, input_post[i][j])






# assert
#published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
#assert(published_title.text == input_post[0])
#print("New article published:", published_title.text)

browser.quit()
