# https://pyttsx3.readthedocs.io/en/latest/engine.html

import pyttsx3

#Creating an Instance
engine = pyttsx3.init()

#Changing voice to Female
# voices = engine.getProperty("voices")
# engine.setProperty("voices", voices[0].id)

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[3].id) 

#Text to speech
engine.say("Hello, I am Ash D")
engine.say("How May I help you")

#Runs the cmds
engine.runAndWait()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()