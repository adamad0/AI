import speech_recognition as sr
from time import sleep
from datetime import datetime
import webbrowser
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty('rate', 150) 

def speak(text):
  engine.say(text)
  engine.runAndWait()
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)

def recognize_voice():
  text = ''

  with sr.Microphone() as source:

    r.adjust_for_ambient_noise(source)

    voice = r.listen(source)

    try:
      text = r.recognize_google(voice)
    except sr.RequestError:
      speak("Sorry, the I can't access the Google API...")
    except sr.UnknownValueError:
      speak("Sorry, Unable to recognize your speech...")
  return text.lower()

def reply(text_version):

  if "date" in text_version:

    date = datetime.now().strftime("%-d %B %Y")
    speak(date)

  if "time" in text_version:

    time = datetime.now().time().strftime("%H %M")
    speak("The time is " + time)
  
  if "song" in text_version:
      search = speak("Which song should I open?")
      url = 'https://open.spotify.com/search/'+search
      webbrowser.get().open(url)
      speak("U are the best listener")


  if "search" in text_version:
    speak("What do you want me to search for?")
    keyword = recognize_voice()
    url = "https://translate.google.com/?sl=auto&tl=tr&text="+keyword
    webbrowser.get().open(url)
  

  if "quit" in text_version or "exit" in text_version or "stop" in text_version:
    speak("Ok, I am going to take a nap...")
    exit()


speak("Hello sir")
sleep(1)
while True:


  text_version = recognize_voice()

  reply(text_version)