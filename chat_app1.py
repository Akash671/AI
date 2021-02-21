"""
@author.    : AKASH KUMAR
@institute. : MIT Institute Moradabad India
@branch.    : Computer Science & Engineering
@work as.   : Software Devloper & Machine Learning Engineer
@website.   : https://medium.com/@akashsaininasa
@github.    : https://github.com/Akash671
@LinkedIn.  : https://www.linkedin.com/in/akash-kumar-52563018a
"""

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)


response = chatbot.get_response("Good morning!")
print(response)
