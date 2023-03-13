import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import sys

import guteFrageClass
import seleniumWebdriverClass


class Login(seleniumWebdriverClass.Test):

    def login(self):
        try:
            wait = seleniumWebdriverClass.Test().wait(10)
            loginButton = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#masthead-toggle-login button')))
            loginButton.click()
            wait = seleniumWebdriverClass.Test().wait(10)
            inputUsername = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#loginform_username_1")))
            inputPassword = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#loginform_password2")))
            submitButton = wait.until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="flyoutcontainer"]/div/div/form/div[4]/button')))

            #username = input("gute-Frage username? ")
            #password = input("gute-Frage password? ")

            username = 'Alaliim'
            password = 'VNqQ@.4yA3-n-@j'

            inputUsername.send_keys(username.strip())
            time.sleep(3)
            inputPassword.send_keys(password.strip())
            time.sleep(2)
            submitButton.click()

            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")




        except Exception as e:
            exit(e)

    def clickCookieMessage(self):
        try:
            wait = seleniumWebdriverClass.Test().wait(10)
            cookieNoticeIframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#sp_message_container_771429 > iframe")))
            seleniumWebdriverClass.Test().driver.switch_to.frame(cookieNoticeIframe)
            seleniumWebdriverClass.Test().driver.find_element(By.CLASS_NAME, 'e2e-accept-button').click()
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
        except Exception as e:
            print('Somethings Wrong, excepting a Cokie Message, trying to proceed with login')

    def do_login(self):
        self.clickCookieMessage()
        self.login()
        time.sleep(10)
