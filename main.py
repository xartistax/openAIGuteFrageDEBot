import loginClass
import guteFrageClass
import seleniumWebdriverClass



login = loginClass.Login()
seleniumWebdriver = seleniumWebdriverClass.Test()
guteFrage = guteFrageClass.guteFrage()

direct_login_url = 'https://www.gutefrage.net/?einstieg=direkt'
home_url = 'https://www.gutefrage.net/home/meine/alle'


seleniumWebdriver.setUp()
seleniumWebdriver.go_to_url(direct_login_url)
login.do_login()

#loop = input("wieviel Antworten? ")


for _ in range(20):
    guteFrage.answeingBot(home_url)

seleniumWebdriver.tearDown()

print("OPERATION FULLY DONE !!!!")
















