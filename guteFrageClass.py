import time
from tkinter import END

from selenium.webdriver.common.by import By
import random

import datetime;

import openAIClass
import seleniumWebdriverClass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
import sys
from selenium.webdriver.support.ui import Select



class guteFrage:



    def check_question(self, home_url):
        wait = seleniumWebdriverClass.Test().wait(100)
        elements = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "article.ListingElement > a")))

        question = elements[0] ## The first question will be answerd
        question_title = question.find_element(By.CLASS_NAME, 'Question-title')
        question_body = question.find_element(By.CLASS_NAME, "ContentBody")

        try:

            return openAIClass.OpenAi().checkAnswer(question_title.text,question_body.text, home_url)

            #return 'answer is here'



        except Exception as e:
            print('Check question failed')
            print(e)

            self.answeingBot(home_url)







    def answeingBot(self, home_url):
        seleniumWebdriverClass.Test().driver.get(home_url)
        randNumber = random.randint(10, 120)
        func_name = sys._getframe().f_code.co_name
        print(func_name + " START")
        if self.wait_until_FirstQuestion_is_no_poll(home_url) == False:
            valid_answer = self.check_question(home_url)
            self.open_question(home_url)
            self.clickOnAnswerButton()
            self.answoring_question(valid_answer, home_url)
            self.send_the_answer(home_url)
            self.writeUrlToFile()




            seleniumWebdriverClass.Test().go_to_url(home_url)
            print(func_name + " is done! now wait " + str(randNumber) + " sec and go on")
            time.sleep(randNumber)
            print(func_name + " STOP")
            return




    def wait_until_FirstQuestion_is_no_poll(self, home_url):
        wait = seleniumWebdriverClass.Test().wait(120)
        try:
            elements = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.ListingElement > a')))
        except:
            self.wait_until_FirstQuestion_is_no_poll(home_url)

        try:
            elements[0].find_element(By.CLASS_NAME, 'ListingElement-poll')
            print('first is a PollQuestion - refresh page in 10 sec and try again')
            self.refresh_try_again(10, home_url)
        except NoSuchElementException:
            try:
                elements[0].find_element(By.CLASS_NAME, 'ListingElement-image')
                print('first is a ImageQuestion - refresh page in 10 sec and try again')
                self.refresh_try_again(10, home_url)
            except NoSuchElementException:
                return False




    def open_question(self, url):
        try:
            wait = seleniumWebdriverClass.Test().wait(120)
            elements = wait.until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, "article.ListingElement > a")))
            elements[0].click()
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
        except:
            self.answeingBot(url)



    def refresh_try_again(self, delay, url):
        time.sleep(delay)
        seleniumWebdriverClass.Test().driver.get(url)
        self.answeingBot(url)
        func_name = sys._getframe().f_code.co_name
        print(func_name + " is done!")

    def clickOnAnswerButton(self,):
        wait = seleniumWebdriverClass.Test().wait(120)
        questionButton = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".QuestionActionBar > button")))
        questionButton.click()
        func_name = sys._getframe().f_code.co_name
        print(func_name + " is done!")

    def answoring_question(self, answer, url):
        func_name = sys._getframe().f_code.co_name
        try:
            wait = seleniumWebdriverClass.Test().wait(120)
            answerField = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".TextEditor.TextEditor--answer .ql-container.ql-snow .ql-editor")))
        except:
            self.answeingBot(url)

        if len(answer)==0:
            self.answeingBot()
            print(func_name + " start allover!")
        else:
            answerField.send_keys(answer)
            # answerField.send_keys('answer here!')
            print(func_name + " is done!")

    def answer_expertise_select(self):
        try:
            dropdown = Select(seleniumWebdriverClass.Test().driver.find_element(By.ID, 'answer-expertise-select'))
            dropdown.select_by_value('PersonalExperience')
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
        except:
            Select(seleniumWebdriverClass.Test().driver.find_element(By.ID, 'answer-expertise-select').click())
            wait = seleniumWebdriverClass.Test().wait(120)
            answerField = wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div[6]/button")))
            answerField.click()
            print(func_name + " is done!")

    def send_the_answer(self, url):
        try:
            button = seleniumWebdriverClass.Test().driver.find_element(By.CSS_SELECTOR, '.WriteAnswerActionBar-submit button')
            button.click()
            func_name = sys._getframe().f_code.co_name
            print(func_name + " is done!")
        except:
            self.answeingBot(url)


    def writeUrlToFile(self):
        with open('log.txt', 'a+') as the_file:
            the_file.write( self.currentDatetime() + ' - ' + self.currentUrl() + '\n')
            #the_file.write( 'okokokokkoko \n')

        func_name = sys._getframe().f_code.co_name
        print(func_name + " is done!")

    def currentDatetime(self):
        current_time = datetime.datetime.now()
        return str(current_time)

    def currentUrl(self):
        current_url = seleniumWebdriverClass.Test().driver.current_url
        return current_url


