# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyttsx3

def speak(text):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[0].id)
    speaker.say(text)
    speaker.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text here: ")
    speak(text)