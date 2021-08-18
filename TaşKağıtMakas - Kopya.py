import speech_recognition as sr
import random


while True:
    zar=["taş","kağıt","makas"]
    zar1=random.choice(zar)
    sonuç1=0
    sonuç2=0
    
    
    r = sr.Recognizer()

    def record(ask = False):
        with sr.Microphone() as source:
            if ask:
                print(ask)
            audio = r.listen(source)
            voice=''
            try:
                voice = r.recognize_google(audio , language='tr-TR')
            except sr.UnkownValueError:
                print("Sizi anlayamadım")
            except sr.RequestError:
                print("sistemi çalıştıramadım")
            return voice
    

    print("Lütfen taş kağıt ya da makastan birisini seçiniz")
    voice = record()
    print(voice)
    

    if voice =="taş"or"kağıt"or"makas":
            print(zar1)
            
    if voice=="Taş" and zar1=="kağıt":
        sonuç2+"1"
        
    
    if voice=="Taş" and zar1=="makas":
        sonuç1+"1"
       
                
    if voice=="Kağıt" and zar1=="taş":
        sonuç1+"1"
       
    
    if voice=="Kağıt" and zar1=="makas":
        sonuç2+"1"
      
    
    if voice=="Makas" and zar1=="taş":
        sonuç2+"1"
       
    
    if voice=="Makas" and zar1=="kağıt":
        sonuç1+"1"
    
    if voice=="sonuç":
        print(sonuç1,sonuç2)
        

    
    
    
    
    if voice =="Ağla":
        print("PEKİ")
        break