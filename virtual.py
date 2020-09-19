import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time

print('Loading your AI personal assistant - G One')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()
