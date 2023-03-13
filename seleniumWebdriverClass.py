from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import sys

class Test:

    @classmethod
    def setUp(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        func_name = sys._getframe().f_code.co_name
        print(func_name + " is done!")

    def go_to_url(self, url):
        self.driver.get(url)
        print ('going to: '+url+' done!')

    def tearDown(self):
        self.driver.close()

    def wait(self, delay):
        return WebDriverWait(self.driver, delay)