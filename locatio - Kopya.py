from geolite2 import geolite2
import socket
import webbrowser
from ip2geotools.databases.noncommercial import DbIpCity
import pyautogui
import time


url= input("Insert a URL:")
IP=socket.gethostbyname(url)

response=DbIpCity.get(IP,api_key="free")

print("IP:",IP)


def iplocation(ip):
    reader = geolite2.reader()
    location = reader.get(ip)


    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
     % (a,b,c,d,e,f,g))


    url = 'https://www.google.com/maps'
    webbrowser.get().open(url)
    time.sleep(2)
    pyautogui.leftClick(x=285, y=173)
    pyautogui.write(d)
    


ip = IP

iplocation(ip)