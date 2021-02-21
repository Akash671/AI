"""
@author.    : AKASH KUMAR
@institute. : MIT Institute Moradabad India
@branch.    : Computer Science & Engineering
@work as.   : Software Devloper & Machine Learning Engineer
@website.   : https://medium.com/@akashsaininasa
@github.    : https://github.com/Akash671
@LinkedIn.  : https://www.linkedin.com/in/akash-kumar-52563018a
"""

#pip install chatterbot


from chatterbot import ChatBot

bot = ChatBot('Norman')

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break


        
