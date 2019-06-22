import pyttsx3
import datetime
import wolframalpha
import wikipedia
import speech_recognition as sr
import webbrowser
import subprocess
import sys
import os
import re

engine = pyttsx3.init()

client = wolframalpha.Client('K7K8Q9-5W2U7U8L7H')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def welcome():
    speak('I am your personal assistant kylie')
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

welcome()

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

    elif 'run' in task:
        search_app = re.search('run (.*)', task)
        app = search_app.group(1)
        print(app)
        os.system(app)
        # subprocess.Popen(["open", "-n", "/Applications/" + app], stdout=subprocess.PIPE)
        # subprocess.Popen(app+'.exe')

    elif 'hello' in task:
        timeHour = datetime.datetime.now().hour
        if timeHour>0 and timeHour<12:
            speak('Hello. Good Morning!')
            print('Kyile: Hello. Good morning!')
        elif timeHour>=12 and timeHour<18:
            speak('Hello. Good Afternoon!')
            print('Kyile: Hello Good Afternoon!')
        else:
            speak('Hello. Good Evening!')
            print('Kyile: Hello Good Evening!') 

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

        
