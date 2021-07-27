import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConduit(object):
    def setup(self):
        self.browser = webdriver.Chrome("/usr/bin/chromedriver")
        self.browser.get("http://localhost:1667")
        self.browser.maximize_window()

    def teardown(self):
        self.browser.quit()

    # # Test_0 HOMEPAGE
    def test__home_page(self):
        time.sleep(2)
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."
        print("conduit HOMEPAGE loaded")

    # # Test_3 ACCEPT COOKIES
    def test__accept_cookies(self):
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
        time.sleep(2)
        print("cookies accepted")

    # # Test_4 REGISTRATION
    def test__registration(self):
        user_input = {"name": "test",
                      "email": "user5@hotmail.com",
                      "password": "Userpass1"
                      }
        self.test__accept_cookies()

        self.browser.find_element_by_xpath('//*[@href="#/register"]').click()
        username = self.browser.find_element_by_xpath('//*[@placeholder="Username"]')
        email = self.browser.find_element_by_xpath('//*[@placeholder="Email"]')
        password = self.browser.find_element_by_xpath('//*[@placeholder="Password"]')

        username.send_keys(user_input["name"])
        email.send_keys(user_input["email"])
        password.send_keys(user_input["password"])
        time.sleep(2)
        self.browser.find_element_by_xpath('//button[1]').click()
        time.sleep(2)
        # assert
        ref_text_fail = "Registration failed!"
        ref_text_success = "Welcome!"
        welcome = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal-title"))
        )
        if welcome.text == ref_text_success:
            print(welcome.text)
            print(self.browser.find_element_by_css_selector(".swal-text").text)
        elif welcome.text == ref_text_fail:
            print(welcome.text)
            print(self.browser.find_element_by_css_selector(".swal-text").text)
#        assert (welcome.text == ref_text_success)
        assert (welcome.text == ref_text_fail)
        print("SIGN UP: ", end="")
        for k, v in user_input.items():
            print(k, v, sep=",", end=";")

        self.browser.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        time.sleep(2)

    # # Test_2 LOGIN user2
    def test__login(self):
        user_login = {"email": "user2@hotmail.com",
                      "password": "Userpass1"
                      }
        self.test__accept_cookies()

        self.browser.find_element_by_xpath('//*[@href="#/login"]').click()
        email = self.browser.find_element_by_xpath('//*[@placeholder="Email"]')
        password = self.browser.find_element_by_xpath('//*[@placeholder="Password"]')
        email.send_keys(user_login["email"])
        password.send_keys(user_login["password"])
        time.sleep(1)
        self.browser.find_element_by_xpath('//button[1]').click()
        time.sleep(1)
        # assert
        user_name = WebDriverWait(
            self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="nav-link" and contains(text(),"user2")]'))
        )
        assert user_name.text == "user2"
        print(f"SIGN IN: as {user_name.text}")
        time.sleep(1)

    # # Test6 NEW POST
    def test__add_new_post(self):
        input_post = ["test", "me", "blabablabal", "key"]
        article_data = ["Article Title", "What's this article about?", "Write your article (in markdown)", "Enter tags"]

        self.test__login()
        self.browser.find_element_by_xpath('//*[@href="#/editor"]').click()
        time.sleep(2)

        fill_article = []
        i = 0
        while i < 3:
            fill = self.browser.find_element_by_xpath(f'//*[@placeholder="{article_data[i]}"]').send_keys(input_post[i])
            fill_article.append(fill)
            i = i + 1

        WebDriverWait(
            self.browser, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//button[1]'))
        ).click()
        time.sleep(2)

        # assert
        published_title = self.browser.find_element_by_xpath('//*[@class="container"]/h1')
        assert (published_title.text == input_post[0])
        print("New article published:", published_title.text)

        # # Test_7 MODIFY POST (title)
    def test__modify_post(self):
        self.test__login()





    # Test_11 LOGOUT user2
    def test__logout(self):
        self.test__login()

        logout_btn = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a/i')
        logout = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a')
        assert(logout.text == ' Log out')
        print("Find logout button:", logout.text)
        time.sleep(2)
        logout_btn.click()
        sign_in = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        assert(sign_in.text == 'Sign in')
        print("Back to homepage:", sign_in.text)
        time.sleep(2)
        print("LOGGED OUT")

