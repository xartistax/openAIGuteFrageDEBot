


import openai

from termcolor import colored

import guteFrageClass
from decouple import config
import sys


class OpenAi:

    try:
        openai.api_key = config('OPEN_API')
    except Exception as e:
        exit(e)


    def checkAnswer(self, question, question_body):
        try:
            blacklist = ["KI", "Als KI", "Als künstliche Intelligenz", "künstliche Intelligenz", "Künstliche Intelligenz", "Als AI", "AI", "künstlicher Intelligenzassistent", "Intelligenzassistent", "digitale Entitität"]
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
                return 'blacklist'

            else:
                return answer
        except Exception as e:
            func_name = sys._getframe().f_code.co_name
            print(colored(func_name.upper() + " That AI model is probebly overloaded with other requests!!!", 'red'))
            exit(colored(e, 'red'))

