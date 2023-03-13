
import os

import openai

from termcolor import colored

import guteFrageClass
from decouple import config


class OpenAi:

    openai.api_key = config('OPEN_API')


    def checkAnswer(self, question, question_body, url):
        blacklist = ["KI", "Als KI", "Als künstliche Intelligenz", "künstliche Intelligenz", "Als AI", "AI"]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "assistant",
                    "content": question + "-" + question_body
                }
            ]
        )
        answer = completion.choices[0].message.content.strip('\n')

        if any([x in answer for x in blacklist]):
            print('Wait 30 Seconds and refresh the pasge because Answer is containin blacklisted words')
            guteFrageClass.guteFrage().refresh_try_again(10, url)

        else:
            print(colored('AI does have an answer !', 'green'))
            return answer
