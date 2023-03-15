# Python ChatGPT Answering-bot (gutefrage.net)

A Simple Answering Bot for Gute-Frage.net

## Description

The Bot is scraping all Questions from the first page. Cleans all questions from Poll and Image Questions and trys to answers them. Blacklistet answers are Ignored. Blacklistet answers are answers who containing word like AI, AI Inteligenz etc.

## Getting Started

### Dependencies

* Programm is running with Python. All required dependencys are in requirements.txt
* Python > 3.0
* [openai.com - ChatGPT API Key](https://platform.openai.com/account/api-keys)

### Installing

1. Clone it
2. Install dependencys from requirements.txt

### Executing program

Run the main.py File


## ToDo next

1. Better Try Catch if the OpenAI API is overloaded with other requests or do a delay after every answering run

2. Dont stop the code if API is overloaded! Sleep some Time and try again


## Authors

Artista  
[@demian_1712](https://instagram.com/demian_1712?)

## Version History

* 0.1
    * Initial dirty Trial run
    * Various bug fixes and optimizations

* 1.0
    * Initial Release

