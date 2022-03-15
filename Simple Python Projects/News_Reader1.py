from win32com.client import Dispatch
import requests
import json

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

url = input("Enter URL : ")
resp = requests.get(url)
txt = resp.text
jos = json.loads(txt)

try:
    speak("The request was accepted")
    speak("Top News of the Day")
    speak(jos)
except Exception as e:
    speak("Sorry! the request was not found !!!")

# https://rapidapi.com/authentication/google/callback?state=%223%22&code=4%2F0AX4XfWiRTqRY9m-Zal0RmP9G56p-mYFXNtwYjI6nd_6Rsnm-jYywVcbjFAw3YOfoZwngXQ&scope=email+profile+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile&authuser=1&prompt=none
# https://newsapi.org/v2/everything?q=tesla&from=2022-02-15&sortBy=publishedAt&apiKey=0cd3a61acd104189953a7506b864022e
