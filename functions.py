import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import openai
import sys






class guteFrage():

    driver = None
    url_2 = 'https://www.gutefrage.net/home/meine/alle'
    login_url = 'https://www.gutefrage.net/?einstieg=direkt';
    options = None

    def __init__(self, *args, **kwargs):
        options = Options()
        options.add_experimental_option("detach", True)
        openai.api_key = "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"


    def goToLoginUrl(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.login_url)



    def login(self):
        try:
            wait = WebDriverWait(self.driver, 100)
            loginButton = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#masthead-toggle-login button')))
            loginButton.click()
            wait = WebDriverWait(self.driver, 100)
            inputUsername = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#loginform_username_1")))
            inputPassword = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#loginform_password2")))
            submitButton = wait.until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="flyoutcontainer"]/div/div/form/div[4]/button')))

            inputUsername.send_keys('alAliim')
            time.sleep(3)
            inputPassword.send_keys('VNqQ@.4yA3-n-@j')
            time.sleep(2)
            submitButton.click()
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
            self.clickCookieMessage(self)


        except Exception as e:
            exit(e)

    def clickCookieMessage(self):
        try:
            wait = WebDriverWait(self.driver, 100)
            cookieNoticeIframe = wait.until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "#sp_message_container_771429 > iframe")))
            self.driver.switch_to.frame(cookieNoticeIframe)
            self.driver.find_element(By.CLASS_NAME, 'e2e-accept-button').click()
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
            self.login()

        except Exception as e:
            exit(e)

    def do_login(self):
        self.goToLoginUrl()
        self.clickCookieMessage()
        self.login()


