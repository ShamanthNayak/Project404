import pyttsx3
import datetime
import wolframalpha
import speech_recognition as sr
import webbrowser
import sys
import os
import re
import wikipedia

engine = pyttsx3.init()

client = wolframalpha.Client('K7K8Q9-5W2U7U8L7H')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def welcome():
    timeHour = datetime.datetime.now().hour
    if timeHour>0 and timeHour<12:
        speak('Good Morning!')
    elif timeHour>=12 and timeHour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am your personal assistant kylie')

# welcome()
speak('What can I do for you')

def command():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print('Listening...')
        r.pause_threshold =  1
        audio = r.listen(source)

    try:
        mycommand = r.recognize_google(audio, language='en-in').lower()
        print('You Said: '+mycommand)
    except sr.UnknownValueError:
        print('...')
        mycommand = command()

    return mycommand

while(True):
    task = command()

    if 'open' in task:
        search_site = re.search('open (.*)', task)
        site = search_site.group(1)
        print('Kylie: Opening '+site)
        speak('Opening '+site)
        if '.' in site:
            webbrowser.open('https://www.'+site)
        else:
            webbrowser.open('https://www.'+site+'.com')

    elif 'time' in task:
        time = datetime.datetime.now()
        print(f'Current time is {time.hour} Hours and {time.minute} Minutes')
        speak(f'Current time is {time.hour} Hours and {time.minute} Minutes')

    elif 'quit' in task or 'bye' in task or 'abort' in task:
        speak('Good bye Have a nice day')
        sys.exit()

    elif 'thank you' in task:
        speak('My pleasure')

    else:
        try:
            res = client.query(task)
            output = next(res.results).text
            print(output)
            speak(output)
        
        except:
            speak('Okay')
            res = wikipedia.summary(task ,sentences=2)
            print(res)
            speak(res)

        
