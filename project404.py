import pyttsx3
import datetime
import wolframalpha
import speech_recognition as sr
import webbrowser

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

# welcome()
speak('What can I do for you')

def command():
    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        print('Listening...')
        r.pause_threshold =  1
        audio = r.listen(source)

    command = r.recognize_google(audio, language='en-in')
    print('User: '+command)

    return command

if __name__=='__main__':
    while(True):
        task = command()
        task = task.lower()

        res = client.query(task)
        output = next(res.results).text
        speak(output)

        if 'open google' in task:
            speak('Opening Google')
            webbrowser.open('www.google.com')
        
        elif 'open youtube' in task:
            speak('Opening Youtube')
            webbrowser.open('www.youtube.com')
