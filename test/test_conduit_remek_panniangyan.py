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


# # # # # # # # # # # # # # # # # # # # # # # # Defining variables # # # # # # # # # # # # # # # # # # # # # # # # 

URL = 'http://localhost:1667'

user_input = {"Username": "user2",
              "Email": "user2@hotmail.com",
              "Password": "Userpass1"
             }

user_login = {"Email": "user2@hotmail.com",
              "Password": "Userpass1"
             }

# Test_6 new post
input_post = ["new", "me", "blabablabal", "key"]  
# Test_7 import data from file
input_file = 'test/input_articles.csv'
# Test_8 modify data
input_post_modify = ["Old title", "én", "lorem ipsum újra meg újra", "kulcs"]
title = "Módositom a cimet"
# Test_9 delete data
input_post_delete = ["Might be deleted", "én", "lorem ipsum újra meg újra", "kulcs"]
# Test_10 write to file
out_file = f"test/{user_name.text}_write_out.csv"

# # # # # # # # # # # # # # # # # # # # # # # # Testing Conduit App # # # # # # # # # # # # # # # # # # # # # # # #

class TestConduit(object):

    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get(URL)
        time.sleep(1)

    def teardown(self):
        self.browser.quit()

# # # # # # # # # # # # # # # # # # # # # # # # Test_0 HOMEPAGE LOADED # # # # # # # # # # # # # # # # # # # # # # # #         
    def test__home_page(self):
        time.sleep(2)
        assert self.browser.find_element_by_xpath('//div[@class="container"]/h1').text == "conduit"
        assert self.browser.find_element_by_xpath('//div[@class="container"]/p').text == "A place to share your knowledge."
        print(f"conduit HOMEPAGE loaded, {self.browser.current_url}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_3 ACCEPT COOKIES # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__accept_cookies(self):
        xpath(self.browser, '//button[contains (.,"I accept!")]').click()
        time.sleep(2)
        assert (self.browser.find_elements_by_xpath('//button') == [])
        time.sleep(1)
        print("Test_3: Cookies accepted")

# # # # # # # # # # # # # # # # # # # # # # # # Test_1 REGISTRATION # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__registration(self):
        accept_cookies(self.browser)
        xpath(self.browser, '//*[@href="#/register"]').click()
        time.sleep(2)
        for k, v in user_input.items():
            xpath(self.browser, f'//*[@placeholder="{k}"]').send_keys(v)
        time.sleep(1)
        xpath(self.browser, '//button[1]').click()
        time.sleep(2)
        # assert
        ref_text_fail = "Registration failed!"
        ref_text_success = "Welcome!"
        welcome = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
        )
        assert (welcome.text == ref_text_success)
        #assert (welcome.text == ref_text_fail)
        print("Test_1 SIGNED UP: ", welcome.text, end=" ")
        if welcome.text == ref_text_success:
            print(self.browser.find_element_by_css_selector(".swal-text").text, sep=" ")
        elif welcome.text == ref_text_fail:
            print(self.browser.find_element_by_css_selector(".swal-text").text, sep=" ")
        for k, v in user_input.items():
            print(k, v, sep=": ", end=";")
        xpath(self.browser, '//*[@class="swal-button swal-button--confirm"]').click()

 # # # # # # # # # # # # # # # # # # # # # # # # Test_2 LOGIN user2 # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__login(self):
        accept_cookies(self.browser)
        xpath(self.browser, '//*[@href="#/login"]').click()
        time.sleep(1)
        for k, v in user_login.items():
            xpath(self.browser, f'//*[@placeholder="{k}"]').send_keys(v)
        time.sleep(1)
        xpath(self.browser, '//button[1]').click()
        time.sleep(1)
        # assert
        user_name = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
        )
        assert user_name.text == "user2"
        print(f"Test_2 SIGNED IN: as {user_name.text}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_4 DATA LISTING # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__list_data(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        # listing active links on homepage
        active_links = self.browser.find_elements_by_xpath('//*[@href="#/"]')
        # assert
        assert(xpath(self.browser, '//*[@href="#/"]') == active_links[0])
        print("Test_4: DATA LISTING - active links on conduit homepage", self.browser.current_url)
        for k in active_links:
            print(k.text)
            
# # # # # # # # # # # # # # # # # # # # # # # # Test_5 PAGINATION # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__pagination(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        # pagination on global feed
        print(f"Test_5 PAGINATION:", end=" ")
        page_list = self.browser.find_elements_by_class_name("page-link")
        for page in page_list:
            page.click()
            print(page.text, sep=", ", end=" ")
        # assert
        last_page = xpath(self.browser, f'//*[@class="page-item active" and @data-test="page-link-{page.text}"]')
        assert (page.text == last_page.text)
        print(f"last page: #{last_page.text}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_6 NEW ARTICLE # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__add_new_article(self):
        article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        xpath(self.browser, '//*[@href="#/editor"]').click()
        time.sleep(2)
        fill_article = []
        i = 0
        while i < len(input_post):
            fill = xpath(self.browser, f'//*[@placeholder="{article_data[i]}"]').send_keys(input_post[i])
            fill_article.append(fill)
            i = i + 1
            time.sleep(1)
        time.sleep(2)
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
        time.sleep(2)
        # assert
        published_title = xpath(self.browser, '//*[@class="container"]/h1')
        publish_date = self.browser.find_element_by_class_name("date")
        assert (self.browser.current_url == f'http://localhost:1667/#/articles/{input_post[0]}')
        print(f"Test_6 New article published with title: \"{published_title.text}\" on {publish_date.text} at {self.browser.current_url}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_7 IMPORT DATA FROM FILE # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__import_data_from_file(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        with open(input_file, 'r') as data:
            csv_reader = reader(data)
            input_post = list(map(tuple, csv_reader))
        print(f"Test_7: {len(input_post)} new articles published from file: {input_file}", end=" ")
        for i in range(1, len(input_post) - 1):     # every line
            xpath(self.browser, '//*[@href="#/editor"]').click()
            time.sleep(2)
            for j in range(0, len(input_post[0])):  # fill the form
                xpath(self.browser, f'//*[@placeholder="{input_post[0][j]}"]').send_keys(input_post[i][j])
            time.sleep(2)
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((By.XPATH, '//button[1]'))).click()
            time.sleep(5)
            # assert
            published_title = xpath(self.browser, '//*[@class="container"]/h1')
            assert (published_title.text == input_post[i][0])
            print(f"{published_title.text}", sep=", ", end="; ")

# # # # # # # # # # # # # # # # # # # # # # # # Test_8 MODIFY POST (title) # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__modify_article(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        add_new_article(self.browser, input_post_modify)
        title_list = []
        title_list.append(title)
        WebDriverWait(self.browser, 5).until(
             EC.visibility_of_element_located((By.XPATH, '//*[@href="#/@user2/"]'))
        ).click()
        time.sleep(2)
        old_title = WebDriverWait(self.browser, 10).until(
             EC.visibility_of_element_located((By.XPATH, '//*[@class="preview-link"]/h1'))
        )
        title_list.append(old_title.text)
        old_title.click()
        time.sleep(2)
        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="article-meta"]/span/a/span'))
        ).click()
        time.sleep(2)
        new_title = WebDriverWait(self.browser, 10).until(
             EC.visibility_of_element_located((By.XPATH, '//*[@placeholder="Article Title"]'))
        )
        new_title.clear()
        new_title.send_keys(title)
        time.sleep(2)
        xpath(self.browser, '//button[@type="submit"]').click()
        time.sleep(5)
        # assert
        new_post_title = WebDriverWait(self.browser, 10).until(
             EC.visibility_of_element_located((By.XPATH, '//*[@class="container"]/h1'))
        )
        title_list.append(new_post_title.text)
        time.sleep(2)
#        assert(self.browser.current_url == f'http://localhost:1667/#/articles/{title_list[2]}')
        assert (title_list[2] == title_list[0])
        print(f"Test_8 DATA MODIFICATION: article title changed: {title_list[1]} -> {title_list[2]}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_9 DELETE ARTICLE # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__delete_article(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        add_new_article(self.browser, input_post_delete)
        time.sleep(2)
        deleted_url = self.browser.current_url
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="article-meta"]/span/button/span'))
        ).click()
        time.sleep(5)
        self.browser.refresh()
        # assert
        assert(self.browser.current_url == 'http://localhost:1667/#/')
        print(f"Test_9: DELETED ARTICLE url: {deleted_url}")


# # # # # # # # # # # # # # # # # # # # # # # # Test_10 SAVE DATA # # # # # # # # # # # # # # # # # # # # # # # # 
    def test__save_data_to_file(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        write_to_file = []
        user_name = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
        )
        write_to_file.append(user_name.text)
        user_name.click()
        time.sleep(2)
        title = xpath(self.browser, '//*[@class="article-preview"]/a/h1').text
        write_to_file.append(title)
        with open(out_file, 'w') as out:
            line = "\n".join(write_to_file)
            out.write(line)
        time.sleep(2)
        # assert
        with open(out_file, 'r') as file:
            list_line = file.read().split("\n")
        assert (list_line == write_to_file)
        print(f"Test_10: WRITE OUT DATA TO FILE, {out_file}: {user_name.text}, {title}")

# # # # # # # # # # # # # # # # # # # # # # # # Test_11 LOGOUT (user2) # # # # # # # # # # # # # # # # # # # # # # # #
    def test__logout(self):
        accept_cookies(self.browser)
        conduit_login(self.browser, user_login)
        logout_btn = xpath(self.browser, '//*[@class="nav-link" and contains(text(),"Log out")]')
        assert(logout_btn.text == ' Log out')
        print("Found logout button:", logout_btn.text)
        logout_btn.click()
        time.sleep(2)
        sign_in_btn = xpath(self.browser, '//*[@href="#/login"]')
        assert(sign_in_btn.text == 'Sign in')
        print("Test_11 LOGGED OUT, Back to homepage:", sign_in_btn.text)
