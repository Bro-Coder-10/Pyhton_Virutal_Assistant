import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                talk('searching...')
    except ImportError:
        pass
    return command


def run_jarvis():
    comman = take_command()
    print(comman)

    if 'play' in comman:
        song = comman.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in comman:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'wiki' in comman:
        question = comman.replace('wiki', '')
        info = wikipedia.summary(question, 2)
        print(info)
        talk(info)

    elif '.com' or 'dot com' in comman:
        web = comman.replace('.com' or 'dot com', '')
        talk('opening...' + web)
        x = 'https://'
        y = web
        z ='.com'
        url = x+y+z
        print(url)
        webbrowser.register('Microsoft Edge', None,
                            webbrowser.BackgroundBrowser
                            ("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
        webbrowser.get('Microsoft Edge').open(url)

    elif 'tell me a joke' in comman:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif comman:
        pywhatkit.search(comman)


while True:
    run_jarvis()
