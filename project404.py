import pyttsx3
import datetime
import wolframalpha
import speech_recognition as sr
import webbrowser
import sys
import os
import wikipedia

engine = pyttsx3.init()

client = wolframalpha.Client('K7K8Q9-5W2U7U8L7H')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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
    speak('I am your personal assistant')

welcome()
speak('What can I do for you')

def command():
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        print('Listening...')
        r.pause_threshold =  1
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language='en-in')
        print('User: '+command)
    except sr.UnknownValueError:
        command()


    return command

if __name__=='__main__':
    while(True):
        task = command()
        task = task.lower()

        if 'open google' in task:
            speak('Opening Google')
            webbrowser.open('www.google.com')
        
        elif 'open youtube' in task:
            speak('Opening Youtube')
            webbrowser.open('www.youtube.com')
        
        elif 'quit' in task or 'bye' in task or 'abort' in task:
            speak('Aborting')
            sys.exit()
        else:
            try:
                res = client.query(task)
                output = next(res.results).text
                print(output)
                speak(output)
            
            except:
                print('Searching Wikipedia')
                speak('Searching Wikipedia')
                res = wikipedia.summary(task ,sentences=2)
                print(res)
                speak(res)

        speak('Next command')

        
