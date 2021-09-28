import pyttsx3 #for the text to speech conversion
import speech_recognition as sr #self explanatory
import json #for storing data persistently
from os import path # for checking if files are present


r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate', 175)

#if the saved_input.txt file does not exist, then
#create it and dump an empty dictionary in it.

if not path.isfile('saved_input.json'):
    dict = {}
    with open('saved_input.json', 'w') as myfile:
        json.dump(dict, myfile)


#if the saved_input.txt file already exists,
#then simply load the file.

with open('saved_input.json', 'r') as myfile:
    dict = json.load(myfile)

#if the count.txt file does not exist, then
#create it and create a variable count. Next
#write the contens of the variable to the
#count.txt file.

if not path.isfile('count.txt'):
    count = 1
    with open('count.txt', 'w') as count_file:
        count_file.write(str(count))

#Method to take the voice input of the user.


def take_input():
    #Get the value of the count variable from
    #a file
    count_file = open('count.txt', 'r')
    count = int(count_file.read())
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        speech = r.recognize_google(audio)
        dict['Reminder ' + str(count)] = speech

        #Save the dictionary mapping of user input in
        #a file

        with open('saved_input.json', 'w') as myfile:
            json.dump(dict, myfile, indent=4)

        #increment the count and save it in an
        #external file so that it can be used
        #for next executions

        count += 1
        count_file = open('count.txt', 'w')
        count_file.write(str(count))

    except sr.UnknownValueError:
        print('Could not fetch Audio. Try again!')

#Method to convert the text to speech


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#Method to list all the user inputs from the saved dictionary


def list_inputs():
    for key, value in dict.items():
        print(key+ ": " +  value)
        text_to_speech(key)
        text_to_speech(' is ')
        text_to_speech(value)

#Prompt the user for the number of inputs they need
n = int(input('How many reminders do you want to set? '))
for i in range(n):
    print('Reminder ' + str(i + 1) + ':')
    take_input()

list_inputs()