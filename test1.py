from types import FrameType
import  pyttsx3
import datetime 
import speech_recognition as sr
import pywhatkit
import wikipedia
engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-US')
        print(query)
        command =takecommand()

        if 'hello' in command:
         speak("Hello sir...")

        elif 'play' in command:
         song=command.replace('play', '')
         speak('playing' + song)
         pywhatkit.playonyt(song)

        elif 'who is' in command:
         person=command.replace('who is', '')
         info=wikipedia.summary(person, 1)
         print(info)
         speak(info)
         
        speak("once again say that please....")
        return 'none'
    return query
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def wishme():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning ")
    elif hour >=12 and hour<18:
        speak("Good afternoon ")
    elif hour >=18 and hour<24:
        speak("Good night ")
  
    speak("Hi.... Deepak")
    speak("The Current date is")
    date()
    speak("The current time is")
    time() 
    speak("Ultron at your service how can i help")
takecommand()
wishme()
