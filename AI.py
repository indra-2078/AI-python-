import abc
import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
from subjects import *
import webbrowser
import smtplib
import pyjokes
import time
import os
import playsound
import random
import ast
import pyautogui
from pytube import YouTube 

words = ["play music", "send emails","tell some jokes", " search wikipedia" , " browse google", "what can i do for you"]
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine. setProperty("rate", 140)
# tif function tells progrema to speak
sub1()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def open_saved(a):
    with open('G:\\My Drive\\Python\\programs\\z\\AI\\new.txt') as f:
        data = f.readline()
        data = (data.replace("}{",","))
    d = ast.literal_eval(data)
    speak(d[a])
    print(d[a])
def onlineclass(sub):
    print(f"joining {sub} class")
    speak(f"joining {sub} class")
    time.sleep(8)
    pos = pyautogui.click(x=617, y=788)
    pos1 = pyautogui.click(x=704, y=808)
    pos2 = pyautogui.click(x=1350, y=566)
    print(pos)
    print(pos1)
    print(pos2)

# def ytdownload(url):
  
#     #link of the video to be downloaded 
#     link=[url
#     ]
  
#     for i in link: 
#         try: 
          
#         # object creation using YouTube
#         # which was imported in the beginning 
#             yt = YouTube(i) 
#         except: 
          
    #     #to handle exception 
    #         print("Connection Error") 
      
    # #filters out all the files with "mp4" extension 
    # mp4files = yt.filter('mp4') 
  
    # # get the video with the extension and
    # # resolution passed in the get() function 
    # d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    # try: 
    #     # downloading the video 
    #     d_video.download("C:\Users\Indra\Downloads") 
    # except: 
    #     print("Some Error!") 
    # print('Task Completed!') 
def save():
    a = "what should i save??"
    print(a)
    z = takeCommand()
    b = speak(a) 
    c = speak("What is it??")
    z1 = takeCommand()
    x = open("new.txt","a")
    x.write(str({z:z1}))
    x.close()  

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("This is crystal, How may i help you")
    
def send_email(to,content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('primemember248@gmail.com','indra@20078')
    server.sendmail('indradhanushhs@gmail.com',
                  to,
                  content)

    server.quit()
def takeCommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        print("suggested commands: ",random.choice(words),";",random.choice(words))
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        global abc
        abc = print("Say that again please...")
        print(abc)
        return "None"
    return query
wish()
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        print("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open" in query:
        list(query)
        web,web1 = query.split()
        web1 = web1.lower()
        web2 = web1 +".com"
        print(f"opening{web1}")
        speak(f"opening{web1}")
        time.sleep(1)
        webbrowser.open(web2)
    elif "time" in query:
        hour = int(datetime.datetime.now().hour)
        print(hour)
        speak(hour)
    elif "play" in query: 
        v = query.replace('play', '')                                 
        a = f"playing{v}..."
        print(a)
        speak(a)
        pywhatkit.playonyt(v)
    elif "what can you do" in query:
        a = "i can play music, i can send emails,i can tell some jokes, i can search wikipedia and i can browse google, what can i do for you"
        print(a)
        speak(a)
        
    elif "email" in query:
        try:  
            z = "To whom should i send: "
            speak(z)
            a = input(z)
            if "@gmail.com" in a:
                speak("What should i say??")
                b = takeCommand()
                send_email(a,b)
                print("Your email has been sent")
                speak("Your email has been sent")
            else:
                print("the gmail is incorrect")
                speak("the gmail is incorrect")
        except Exception as e:
            print(e) 
    elif "joke" in query:
        a1 = pyjokes.get_joke()
        print(a1)
        speak(a1)
    elif "google" in query:
        a = query.replace("google","")
        webbrowser.open(a)
    elif "exit" in query or "quit" in query:
        speak("quitting...")
        time.sleep(2)
        break 
    elif "save" in query:
         save()
    elif "information" in query:
        a = speak("which one should i open??")
        b = takeCommand()
        open_saved(b)
    elif "games" in query:
        speak("Searching results on google...")
        time.sleep(2)
        speak("Found a platform of online games , opening it!!")
        webbrowser.open("https://www.arkadium.com/games/")
    elif "search youtube" in query:
        speak("What is that i have to search??")
        a = takeCommand()
        b = "https://www.youtube.com/results?search_query="+a
        webbrowser.open(b)
    elif "kannada" in query:
        webbrowser.open("https://meet.google.com/njv-juak-bkv")
        onlineclass("kannada")
    elif "english" in query:
        webbrowser.open("https://meet.google.com/fwv-eewz-xpp")
        onlineclass("english")
    elif "maths" in query or "mathematics" in query:
        webbrowser.open("https://meet.google.com/bjj-dyvc-wyd")
        onlineclass("mathematics")
    elif "social" in query or "social science" in query:
        webbrowser.open("https://meet.google.com/cks-gfyt-noo")
        onlineclass("social science")
    elif "physics" in query:
        webbrowser.open("http://meet.google.com/nis-mkau-fub")
        onlineclass("physics")
    elif "chemistry" in query:
        webbrowser.open("https://meet.google.com/dbd-suvg-tnz")
        onlineclass("chemistry")
    elif "biology" in query:
        webbrowser.open("https://meet.google.com/xvx-kejw-ioo")
        onlineclass("biology")
    elif "mic" in query or "mike" in query:
        try:
            pos = pyautogui.click(x=617, y=788)
            pos1 = pyautogui.click(x=816, y=965)
        except:
            print("Sorry cant turn on your mic")
    elif "camera" in query:
        try:
            pos = pyautogui.click(x=704, y=808)
            pos1 = pyautogui.click(x=885, y=966)
        except:
            print("Sorry cant turn on your camera")
    elif "present" in query:
        pos4 = pyautogui.click(x=948, y=968)
        pos5 = pyautogui.click(x=1105, y=799)
    elif "tired" in query:
        speak("I think you must take rest, shall i play a song from my playlist that can make your mood relaxed")
        a = takeCommand()
        if "yes" in a:
            speak("playing faded")
            webbrowser.open("https://www.youtube.com/watch?v=pIWaVJPl0-c&list=PL_t_KoYo7XXXdetWY9FVcV7T3gpMTUZK3")
    elif "playlist" in query:
        speak("I think you must take rest, shall i play a song from my playlist that can make your mood relaxed")
        a = takeCommand()
        if "yes" in a:
            speak("playing faded")
            webbrowser.open("https://www.youtube.com/watch?v=pIWaVJPl0-c&list=PL_t_KoYo7XXXdetWY9FVcV7T3gpMTUZK3")
        elif "no" in a:
            speak("ok what shall i do??")
            takeCommand()
        else:
            takeCommand()
    elif "vs code" in query:
        os.startfile("\\Visual Studio Code.lnk")
    elif "chrome" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
    elif "run whatsapp" in query:
        os.startfile("C:\\Users\\Indra\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp.lnk")
    elif "sustainable" in query:
        print("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary("sustainable development")
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif abc == None :
        pass
    else:
        pass