


import openai

from termcolor import colored

import guteFrageClass
from decouple import config


class OpenAi:

    try:
        openai.api_key = config('OPEN_API')
    except Exception as e:
        exit(e)


    def checkAnswer(self, question, question_body):
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
