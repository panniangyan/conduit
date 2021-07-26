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

    def teardown(self):
        self.browser.quit()

    # # Test0 HOMEPAGE
    def test__home_page(self):
        time.sleep(2)
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1').text == "conduit"
        assert self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/p').text == "A place to share your knowledge."
        print("conduit HOMEPAGE loaded")

    # # Test1 ACCEPT COOKIES
    def test__accept_cookies(self):
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
        time.sleep(2)
        print("cookies accepted")

    # Test2 LOGIN user2
    def test__login(self):
        self.browser.maximize_window()
        self.test__accept_cookies()
        self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
        email = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[1]/input')
        password = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset[2]/input')
        email.send_keys("user2@hotmail.com")
        time.sleep(1)
        password.send_keys("Userpass1")
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(1)
        user_name = WebDriverWait(
            self.browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/nav/div/ul/li[4]/a'))
        )
        assert user_name.text == "user2"
        print(f"LOGIN: as {user_name.text}")
        time.sleep(1)
        self.test__home_page()

    # Test11 LOGOUT user2
    def test__logout(self):
        self.browser.maximize_window()
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

    # # Test6 NEW POST
    def test__add_post(self):
        self.browser.maximize_window()
        self.test__login()
        new_article = self.browser.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
        new_article.click()
        time.sleep(5)

        input_post = ("test", "me", "blabablabal", "key")
        article = []
        for i in range(4):
            if i == 2:
                article[i] = WebDriverWait(
                    self.browser, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, f'//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[{i + 1}]/textarea'))
                )
                article[i + 1].send_keys(input_post[i + 1])
            else:
                article[i] = WebDriverWait(
                    self.browser, 5).until(
                    EC.visibility_of_element_located((By.XPATH, f'//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[{i+1}]/input'))
                )
                article[i+1].send_keys(input_post[i+1])



#        article_title = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[1]')
#        article_about = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]')
#        article[2] = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
#        article[3] = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[4]/')

 #       article_title.send_keys("title")
 #       article_about.send_keys("me")
 #       article_text.send_keys("blablabla")
  #      article_tag.send_keys("key")
        time.sleep(2)

        publish_btn = WebDriverWait(
            self.browser, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/div/div/div/form/button'))
            )
#        publish_btn = self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')
        publish_btn.click()
        time.sleep(5)

        published_title = self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/h1')
        assert(published_title.text == article[0].text)
        print("New article published:", published_title.text)

    def test__list_elements(self):
        self.browser.maximize_window()
        self.test__accept_cookies()


