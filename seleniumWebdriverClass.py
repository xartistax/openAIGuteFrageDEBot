from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import sys
from termcolor import colored
class Test:

    @classmethod
    def setUp(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        func_name = sys._getframe().f_code.co_name
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))

    def go_to_url(self, url):
        self.driver.get(url)
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))

    def tearDown(self):
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))

    def wait(self, delay):
        return WebDriverWait(self.driver, delay)