import requests, json

print ("IP","Ülke","İl","İlçe","Enlem","Boylam")

ip = ["142.250.184.142"]
APIKEY = "2ded3df6d0408ded241cee2c18bfc8f0"
for x in ip:
  serviceURL = "http://api.ipapi.com/"+x+"?access_key="+APIKEY+"&output=json"  
  r = requests.get(serviceURL)
  y = json.loads(r.text)
  print(y["ip"],y["country_name"],y["region_name"],y["city"],y["latitude"],y["longitude"])  