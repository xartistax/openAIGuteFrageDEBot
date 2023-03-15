import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import sys

import guteFrageClass
import seleniumWebdriverClass

from termcolor import colored


class Login(seleniumWebdriverClass.Test):

   

    def send_keys_and_submit(self, home_url):
        wait = seleniumWebdriverClass.Test().wait(120)
        inputUsername = wait.until(ec.presence_of_element_located((By.ID, "loginform_username_1")))
        inputPassword = wait.until(ec.presence_of_element_located((By.ID, "loginform_password2")))
        submitButton = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="flyoutcontainer"]/div/div/form/div[4]/button')))

        time.sleep(3)
        inputUsername.send_keys('AlmaerifatQua')
        time.sleep(3)
        inputPassword.send_keys('VNqQ@.4yA3-n-@j')
        time.sleep(3)
        submitButton.click()
        time.sleep(3)

        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))



        
        

        

    def click_login_btn(self, home_url):
        wait = seleniumWebdriverClass.Test().wait(120)
        loginButton = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#masthead-toggle-login button')))
        loginButton.click()
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))

            

    def clickCookieMessage(self, home_url):
        func_name = sys._getframe().f_code.co_name
        wait = seleniumWebdriverClass.Test().wait(120)

        cookieNoticeIframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#sp_message_container_771429 > iframe")))


        seleniumWebdriverClass.Test().driver.switch_to.frame(cookieNoticeIframe)
        seleniumWebdriverClass.Test().driver.find_element(By.CLASS_NAME, 'e2e-accept-button').click()
        print(colored(func_name.upper() + " done !", 'green'))


    def do_login(self, home_url):
        self.clickCookieMessage(home_url)
        self.click_login_btn(home_url)
        self.send_keys_and_submit(home_url)
        seleniumWebdriverClass.Test().go_to_url(home_url)
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))



    


    