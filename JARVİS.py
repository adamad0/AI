import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import pywhatkit as kit
import wikipedia
import phonenumbers
from phonenumbers import geocoder
import speedtest 
import pyautogui

s=speedtest.Speedtest()




r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice=''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnkownValueError:
            speak("Ne dion la")
        except sr.RequestError:
            speak("bişiler ters gitti moruq")
        return voice

saat=(datetime.now().strftime('%H:%M:%S'))

def response(voice):
    
    
    if "saat" in voice:
        speak(saat)
    
    if "arama" in voice:
        search = record("ne aramak istiyorsunuz?")
        url = 'https://google.com//search?q='+search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım bunlar")
     
    if "video" in voice:
        search = record("hangi videoyu açmak istiyorsunuz?")
        url = 'https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        speak(search + "için bulduklarım bunlar")
        
    if "şarkı" in voice:
        search = record("hangi şarkıyı açmak istiyorsunuz?")
        url = 'https://open.spotify.com/search/'+search
        webbrowser.get().open(url)
        speak("müzik zevkinize hayran kaldım")
    
    if "araştırma yap" in voice:
        search = record("wikipedia da ne araştırmak istiyorsunuz?")
        url = 'https://tr.wikipedia.org/wiki/'+search
        webbrowser.get().open(url)
        speak(search + "için wikipediada bulduklarım bunlar")
        
        
    if "ara" in voice:
        search = record("Wikipedia da ne araştırmak istiyorsunuz")
        result = wikipedia.summary(search)
        url = "https://translate.google.com/?sl=auto&tl=tr&text="+result
        webbrowser.get().open(url)
    
    if "toplantı" in voice:
        url = 'https://meet.google.com/?authuser=1'
        webbrowser.get().open(url)
        speak("toplantınızı buradan bulabilirsiniz")
        
    
    if "kişisel" in voice:
        url = 'https://meet.google.com/landing?authuser=0'
        webbrowser.get().open(url)
        speak("kişisel toplantınızı buradan bulabilirsiniz")
        
    
    if "internet" in voice:
        speak("internetinizi test ediyorum")

        indirmehızı=s.download()/1048576
        yüklemehızı=s.upload()/1048576
        ping=round(s.results.ping)

        speak(f"indirme hızı:{indirmehızı:.2f}Mbps")
        speak(f"yükleme hızı:{yüklemehızı:.2f}Mbps")
        speak(f"ping:{ping:.2f}Mbps")

    if "oyuncu ara" in voice:
        search = record("hangi oyuncunun ligini aramak istiyorsunuz?")
        url = 'https://www.leagueofgraphs.com/tr/summoner/tr/'+search
        webbrowser.get().open(url)
        speak(search,"'nun ligini burada buldum")
        
    
    
    if "çevir" in  voice:
        search = record("çevirmek istediğiniz kelime nedir?")
        url = "https://translate.google.com/?sl=auto&tl=tr&text="+search
        webbrowser.get().open(url)
        
    
    if "kanser" in voice:
        os.system("start desktop\LeagueofLegends")
        speak("Kanser uygulaması açılıyor")
        pyautogui.write("adamado05")
        pyautogui.press("Tab")
        pyautogui.write("*********")
        pyautogui.press("Enter")
    
    if "valorant" in voice:
        os.system("start desktop\Valorant")
        speak("Valorant açılıyor")
        

        
    


    if "mesaj" in voice:
        speak("x'a ne söylemek istersiniz")
        a=input("Lütfen mesaj göndermek için bir tel nosu girin")
        b=input("Mesajınızı girin")
        time.sleep(3)
        
        phone=phonenumbers.parse(a)
        speak(geocoder.description_for_number(phone,"tr"))
        kit.sendwhatmsg(a,b,0,11)
        

    
    if "tamamdır" in voice:
        speak("istediğiniz zaman buradayım")
        exit()
        


def speak(string):
    tts = gTTS(string,lang='tr')
    rand= random.randint(1,100000)
    file = "audio-"+str(rand) +'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
        
speak("emrinizdeyim")
time.sleep(0.5)
while 1:
    voice = record()
    response(voice)
