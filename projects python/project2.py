# MY SECOND PROJECT
# WEATHER APP


import requests
import json
import pyttsx3

city = input("Enter the name of the city:\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
print(r.text)
wether = json.loads(r.text)
w = wether["current"]["temp_c"]
x = wether["current"]["last_updated"]

if __name__ == '__main__':
    text_to_speech = pyttsx3.init()

word = f"The current weather in {city} is {w} degree and its last updated on {x}"
text_to_speech.say(word)
text_to_speech.runAndWait()



