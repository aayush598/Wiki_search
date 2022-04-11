#Wikipedia search

import pyttsx3

# setting engine
engine=pyttsx3.init()

# change voice to female
voices=engine.getProperty('voices')
voices=engine.setProperty('voice',voices[1].id)

# slow down the speed
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

# searching from wikipedia
import wikipedia
def wiki_search(topic):
    result=wikipedia.summary(topic,sentences=4)
    print(result)
    engine.say(result)
    engine.runAndWait()
topic=input('Enter the topic: ')
wiki_search(topic)
