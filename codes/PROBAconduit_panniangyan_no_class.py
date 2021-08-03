import time
import csv
from csv import reader
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver_options = Options()
driver_options.headless = True
browser = webdriver.Chrome(ChromeDriverManager().install(), options=driver_options)


def test_setup():
    browser.get("http://localhost:1667")
    browser.maximize_window()
    time.sleep(1)

def test_teardown():
    browser.quit()

# # Test_3 ACCEPT COOKIES
def test__accept_cookies():
    setup()
    browser.find_element_by_xpath('//button[contains (.,"I accept!")]').click()
    time.sleep(2)
    assert (browser.find_elements_by_xpath('//button') == [])
    time.sleep(1)
    print("Test_3: cookies accepted")

# # Test_1 REGISTRATION
def test__registration():
    user_input = {"name": "test",
                  "email": "user5@hotmail.com",
                  "password": "Userpass1"
                 }
    test__accept_cookies()

    browser.find_element_by_xpath('//*[@href="#/register"]').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@placeholder="Username"]').send_keys(user_input["name"])
    browser.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(user_input["email"])
    browser.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(user_input["password"])
    time.sleep(1)
    browser.find_element_by_xpath('//button[1]').click()
    time.sleep(2)
     # assert
    ref_text_fail = "Registration failed!"
    ref_text_success = "Welcome!"
    welcome = WebDriverWait(browser, 5).until(
         EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
    )
    # assert (welcome.text == ref_text_success)
    assert (welcome.text == ref_text_fail)
    print("Test_1 SIGNED UP: ", welcome.text, end=" ")
    if welcome.text == ref_text_success:
        print(browser.find_element_by_css_selector(".swal-text").text, sep=" ")
    elif welcome.text == ref_text_fail:
        print(browser.find_element_by_css_selector(".swal-text").text, sep=" ")
    for k, v in user_input.items():
        print(k, v, sep=": ", end=";")
    browser.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
    time.sleep(1)

# # Test_2 LOGIN user2
def test__login():
    user_login = {"email": "user2@hotmail.com",
                  "password": "Userpass1"
                  }
    test__accept_cookies()

    browser.find_element_by_xpath('//*[@href="#/login"]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@placeholder="Email"]').send_keys(user_login["email"])
    browser.find_element_by_xpath('//*[@placeholder="Password"]').send_keys(user_login["password"])
    time.sleep(1)
    browser.find_element_by_xpath('//button[1]').click()
    time.sleep(1)
    # assert
    user_name = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
        )
    assert user_name.text == "user2"
    print(f"Test_2 SIGNED IN: as {user_name.text}")
    time.sleep(1)

# # Test_4 DATA LISTING
def test__list_data():
    test__login()
    active_links = browser.find_elements_by_xpath('//*[@href="#/"]')
    # assert
    assert(browser.find_element_by_xpath('//*[@href="#/"]') == active_links[0])
    print("Test_4: DATA LISTING - active links on conduit homepage", browser.current_url)
    for k in active_links:
        print(k.text)
        
 # # Test_5 PAGINATION
 def test__pagination():
     test__login()
     # pagination on global feed
     print(f"Test_5 PAGINATION:", end=" ")
     page_list = browser.find_elements_by_class_name("page-link")
     for page in page_list:
        page.click()
        print(page.text, sep=", ", end=" ")
     # assert
     last_page = browser.find_element_by_xpath(f'//*[@class="page-item active" and @data-test="page-link-{page.text}"]')
     assert (page.text == last_page.text)
     print(f"last page: #{last_page.text}")
     time.sleep(1)

    # # Test_6 NEW ARTICLE
    def test__add_new_article():
        input_post = ["test", "me", "blabablabal", "key"]
        article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

        test__login()
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
        time.sleep(2)
        # assert
        published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
        publish_date = browser.find_element_by_class_name("date")
        assert (published_title.text == input_post[0])
        print(f"Test_6 New article published with title: \" {published_title.text} \" on {publish_date.text} at {browser.current_url}")
        time.sleep(1)

    # # Test_7 IMPORT DATA FROM FILE
    def test__import_data_from_file():
        test__login()
        input_file = 'input_article.csv'
        with open(input_file, 'r') as data:
            csv_reader = reader(data)
            input_post = list(map(tuple, csv_reader))
        print(f"Test_7: {len(input_post)} new articles published from file: {input_file}", end=" ")
        for i in range(1, len(input_post) - 1):     # every line
            browser.find_element_by_xpath('//*[@href="#/editor"]').click()
            time.sleep(2)
            for j in range(0, len(input_post[0])):  # fill the form
                browser.find_element_by_xpath(f'//*[@placeholder="{input_post[0][j]}"]').send_keys(input_post[i][j])
            time.sleep(2)
            WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
            time.sleep(2)
            # assert
            published_title = browser.find_element_by_xpath('//*[@class="container"]/h1')
            assert (published_title.text == input_post[i][0])
            print(f"{published_title.text}, {input_post[i][0]}", sep=", ", end="; ")
        time.sleep(1)

    # # Test_8 MODIFY POST (title)
    def test__modify_article():
        test__login()
        title_list = []
        title = "OhLALA"
        title_list.append(title)
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@user2/"]'))
        ).click()
        time.sleep(4)
        old_title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="preview-link"]/h1'))
        )
        title_list.append(old_title.text)
        old_title.click()
        time.sleep(4)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="article-meta"]/span/a'))
        ).click()
        time.sleep(2)
        new_title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@placeholder="Article Title"]'))
        )
        new_title.clear()
        new_title.send_keys(title)
        time.sleep(2)
        browser.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(5)
        # assert
        new_post_title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="container"]/h1'))
        )
        title_list.append(new_post_title.text)
        time.sleep(2)
        assert (title_list[2] == title_list[0])
        print(f"Test_8 DATA MODIFICATION: article title changed: {title_list[1]} -> {title_list[2]} (input: {title_list[0]})")
        time.sleep(1)

    # # Test_9 DELETE ARTICLE
    def test__delete_article():
        test__login()
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@user2/"]'))
        ).click()
        time.sleep(4)
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="preview-link"]/h1'))
        ).click()
        time.sleep(4)
        deleted_url = browser.current_url
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/span/button/span'))
        ).click()
        time.sleep(5)
        browser.refresh()
        # assert
        assert(browser.current_url == 'http://localhost:1667/#/')
        print(f"Test_9: DELETED ARTICLE url: {deleted_url}")
        time.sleep(1)

    # # Test_10 SAVE DATA
    def test__save_data_to_file():
        test__login()
        user_name = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
        )
        user_name.click()
#        out_file = "{user_name.text}_title.csv"
        time.sleep(2)
        title = browser.find_element_by_xpath('//*[@class="article-preview"]/a/h1').text
        with open(f'{user_name.text}_title.csv', 'w') as out:
            out.write(title)
        time.sleep(2)
        # assert
        with open(f'{user_name.text}_title.csv', 'r') as file:
            assert(file.read() == title)
        print(f"Test_10: WRITE TO FILE {user_name.text}_title.csv, {title}")

    # Test_11 LOGOUT (user2)
    def test__logout():
        test__login()
        logout_btn = browser.find_element_by_xpath('//*[@class="nav-link" and contains(text(),"Log out")]')
        assert(logout_btn.text == ' Log out')
        print("Found logout button:", logout_btn.text)
        logout_btn.click()
        time.sleep(2)
        sign_in_btn = browser.find_element_by_xpath('//*[@href="#/login"]')
        assert(sign_in_btn.text == 'Sign in')
        print("Test_11 LOGGED OUT, Back to homepage:", sign_in_btn.text)
        time.sleep(2)


