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
from termcolor import colored

class guteFrage:



    def answeringBot(self, home_url):

        func_name = sys._getframe().f_code.co_name
        questions = self.get_all_questions()
        sorted_questions = self.sort_questions(questions)
        shuffled_questions = self.shuffle_questions (sorted_questions)
        answerd_questions = self.answering_all_sorted_questions(shuffled_questions)
        answerd_questions_clean = self.clean_blacklist_answers(answerd_questions)

        self.post_all_answers(answerd_questions_clean, home_url)



        print(colored(func_name.upper() + " done !", 'green'))

    

    def shuffle_questions(self, questions):
        random.shuffle(questions)
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))
        return questions
        


    def get_all_questions(self):
        wait = seleniumWebdriverClass.Test().wait(120)
        elements = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'article.ListingElement > a')))
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))
        return elements

    def question_count(self, questionList):
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))
        return len(questionList)




    
    

    def sort_questions(self, questions):
        func_name = sys._getframe().f_code.co_name
        sorted_questions = []

        for question in questions:

            isPoll = len(question.find_elements(By.CLASS_NAME, 'ListingElement-poll')) > 0
            isImage = len(question.find_elements(By.CLASS_NAME, 'ListingElement-image')) > 0

            if isPoll == False and isImage == False:


                question_title = question.find_element(By.CLASS_NAME, 'Question-title').text
                question_body = question.find_element(By.CLASS_NAME, "ContentBody").text
                question_link = question.get_attribute('href')
                dictionary = {
                    "title" : question_title ,
                    "question" : question_body ,
                    "url" : question_link
                    }
                sorted_questions.append(dictionary)

        print(colored(func_name.upper() + " done !", 'green'))
        return sorted_questions



    def get_amount(self, max):
        while True:
            amount = input("Es gibt " + str(max) + " Fragen zu beantworten! Wieviel sollen beantwortet werden? ")
            try:
                val = int(amount)
                if val > max or val == 0:
                    self.get_amount(max)
                else:
                    return val
                break
            except ValueError:
                print("Muss eine Zahl seine")


    def answering_all_sorted_questions(self, questions):
        func_name = sys._getframe().f_code.co_name
        answerd_questions = []
        i = 1



        amount = self.get_amount(len(questions))

        for question in questions[:amount]:
            print(colored("✔ Question " + str(i) + " of " + str(amount) + " - start!...", 'cyan'))
            answer = openAIClass.OpenAi().checkAnswer(question['title'],question['question'])
            dictionary = {
                "title" : question['title'] ,
                "question" : question['question'] ,
                "url" : question['url'], 
                "answer" : answer
                }
            answerd_questions.append(dictionary)
            print(colored("✔ Question " + str(i) + " of " + str(amount) + " - done !", 'cyan'))
            i +=1

        
        return answerd_questions


        

        


    def clean_blacklist_answers(self, questions):
        func_name = sys._getframe().f_code.co_name
        clean_answers = []

  
        for question in questions:
            if question['answer'] != 'blacklist':
                clean_answers.append(question)
        
        if len(clean_answers) == 0:
            exit( print(colored("NACH BLACKLISTCHECK BLIEBEN KEINE FRAGEN MEHR ÜBRIG - VERSUCHS NOCHMAL", 'magenta')) )
    
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + "NACH BLACKLISTCHECK BLIEBEN NOCH " + str(len(clean_answers))+ " ÜBRIG", 'magenta'))
        print(colored(func_name.upper() + " done !", 'green'))

        return clean_answers
        

    def writeUrlToFile(self):
        with open('log.txt', 'a+') as the_file:
            the_file.write( self.currentDatetime() + ' - ' + self.currentUrl() + '\n')
        func_name = sys._getframe().f_code.co_name
        print(colored(func_name.upper() + " done !", 'green'))

    def currentDatetime(self):
        current_time = datetime.datetime.now()
        
        return str(current_time)

    def currentUrl(self):
        current_url = seleniumWebdriverClass.Test().driver.current_url
        return current_url

    
    def post_all_answers(self, questions, home_url):

        
        i = 1

        for question in questions:
            delay = random.randint(30,120 )
            delay_two = random.randint(5, 12 )
            func_name = sys._getframe().f_code.co_name
            seleniumWebdriverClass.Test().go_to_url(question['url'])
            wait = seleniumWebdriverClass.Test().wait(10)
            time.sleep(delay_two)
            questionButton = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".QuestionActionBar > button")))
            questionButton.click()
            answerField = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".TextEditor.TextEditor--answer .ql-container.ql-snow .ql-editor")))
            answerField.send_keys(question['answer'])
            button = seleniumWebdriverClass.Test().driver.find_element(By.CSS_SELECTOR, '.WriteAnswerActionBar-submit button')
            button.click()
            self.writeUrlToFile()
            
            seleniumWebdriverClass.Test().go_to_url(home_url)


            
            print((colored(func_name.upper() + " Posted " + str(i) + " Answer of "+ str(len(questions)) +"! delay before next post : " + str(delay) + " seconds"   ,'red', 'on_black', ['bold', 'blink'])))
            print((colored(func_name.upper() + " done !", 'green')))

            i +=1

            time.sleep(delay)


        