# https://pyttsx3.readthedocs.io/en/latest/engine.html


import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('Hello, I am Ash D, Your personal Assistant.')
   engine.say('How may I help you')
engine.runAndWait()