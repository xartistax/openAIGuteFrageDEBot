import loginClass
import guteFrageClass
import seleniumWebdriverClass
import openAIClass
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


login = loginClass.Login()
seleniumWebdriver = seleniumWebdriverClass.Test()
guteFrage = guteFrageClass.guteFrage()

direct_login_url = 'https://www.gutefrage.net/?einstieg=direkt'
home_url = 'https://www.gutefrage.net/home/meine/alle'
how_many_questions = 3

seleniumWebdriver.setUp()
seleniumWebdriver.go_to_url(direct_login_url)


login.do_login(home_url) 
guteFrage.answeringBot(home_url)    





#seleniumWebdriver.tearDown()




