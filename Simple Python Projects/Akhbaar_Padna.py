# The task you have to perform is to read the news using python. Build a program that will give you daily top 10 latest news. For that, you have to check the website  https://newsapi.org/ which gives the news API. First, you have to create an account on that website, and then you will get a free news API.
#
# What you have to do is :
#
# You have to get the most relevant and latest news API from https://newsapi.org/. Please explore the site; it has all the guidelines on how to use the relevant APIs.
# After you have the news API, you have to install the package using the statement:


import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for today.. Lets Begin")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-02-21&sortBy=publishedAt&apiKey=0cd3a61acd104189953a7506b864022e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..Listen Carefully")
    speak("Thanks for listening ... ")
