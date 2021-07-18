import ctypes
import json
import datetime
import smtplib
import subprocess
import time
import webbrowser
from typing import Final

from clint.textui import progress


import ec
import progress
import pyautogui as pt
import bs4
import pywhatkit as pywhatkit

import wolframalpha
from googletrans import Translator
from urllib.request import urlopen
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup

engine = pyttsx3.init()
rate = engine.getProperty("rate")
# print(voices[1].id)
engine.setProperty('rate', 'rate-zh')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

    speak("I am angela sir. please tell me what to do")


def sendEmail(to, content):
    sender_mail = 'pp728776@gmail.com'
    password = 'patelscompany'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_mail, password)
    server.sendmail(sender_mail, to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        query = None
    return query


def takeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        query = None

    return query.lower()


def Tran():
    speak("Tell me your line ")
    line = takeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)


def WolfRam(query):
    api_key = "6HLAEY-EERG65HRU2"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:

        Answer = next(requested.results).text

        return Answer

    except:

        speak("an string value is not answerable.")


# Python program to
# demonstrate creation of an
# assistant using wolf ram API


def Calculator(query):
    Term = str(query)
    Term = Term.replace("angela", "")
    Term = Term.replace("calculate", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("into", "*")

    Final = str(Term)

    try:
        result = WolfRam(Final)
        print(f"{result}")
        speak(f"{result}")

    except:
        speak("an string value is not answerable.")


def CoronaVirus(country):
    countries = str(country).replace(" ", "")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)
    soups = bs4.BeautifulSoup(result.text, 'html.parser')
    corona = soups.find_all('div', class_='maincounter-number')

    Data = []

    for case in corona:
        span = case.find('span')

        Data.append(span.string)

    cases, Death, Recovered = Data
    return cases, Death, Recovered
    print(f"cases :{cases}")
    print(f"deaths : {Death}")
    print(f"recovered :{Recovered}")

if __name__ == '__main__':


    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Piyush.")

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'i am' in query or 'my name' in query:
            print("nice name")
            speak('nice name')

        elif 'your name' in query:
            print("I am angela sir what is your name")
            speak("I am angela sir what is your name")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you are fine")

        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Piyush. further It's a secret")

        elif 'weather' in query:
            speak("opening weather forecast")
            speak(" for which city do you want to check")
            city_name = takeCommand()
            search = f"temperature of {city_name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"the temperature is {temp}")

        elif 'anshika' in query:
            print("she is fat ugly girl of 101 kg weight")
            speak("she is fat ugly girl of 101 kg weight")

        elif 'are you serious' in query:
            speak("I am not joking")
            print("and actually I am also confused that how can she be my master's sister")
            speak("and actually I am also confused that how can she be my master's sister")

        elif 'pranshu' in query:
            speak("I am searching for pranshu")
            print("ohh wow he is a smart and good looking guy with a nice hair design")
            speak("ohh wow he is a smart and good looking guy with a nice hair design")

        elif 'love' in query:
            print("No my master told me to never fall in love but i like you ")
            speak("No my master told me to never fall in love but i like you ")

        elif 'marry' in query:
            print("yeah I can marry you if you come to my world")
            speak(" yeah I can marry you if you come to my world")

        elif 'master' in query:
            print("my master is Piyush Patel")
            speak("my master is Piyush Patel")

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ppp166544@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Piyush, I couldn't send the email")

        elif 'translate' in query:
            Tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = query.replace("jarvis", "")
            speak("you tell me to remind me that :" + rememberMsg)
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt', 'r')
            speak('you told me to :' + remember.read())

        elif 'calculate' in query:
            speak('what do you want to calculate')
            query = input('give input:  ')
            Calculator(query)

        elif 'coronavirus' in query:
            speak('which country information do you want to know')
            country = takeCommand()
            CoronaVirus(country)

        elif "send message" in query:
            pywhatkit.sendwhatmsg('+917880535605', 'hello piyush bhai....', 16, 30)  # number  /  #msg you want to send
            # time hur,sec.

        elif 'open automation' in query:

            limit = input("enter limit")
            message = input("enter msg:")
            i = 0

            time.sleep(5)
            while i < int(limit):
                pt.typewrite(message)
                pt.press("enter")
                i += 1

        elif 'functions' in query:
            print(
                'I can tell you time,weather of any city,coronavirus update of any country,calculate,sendEmail,Watsapp messages,Message Automation,Screenrecording,Open googleand youtube,Search Wikipedia,Set Reminder, Translate Hindi to English sentences,Tell you a joke.')


        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey 
                    =\\ee8475822985434fa71a57b5c583ac7c\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')


        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "space news" in query:
            speak("tell me the date for news extraction")
            Date = input('Date: ')
            from nasa import NasaNews
            NasaNews(Date)