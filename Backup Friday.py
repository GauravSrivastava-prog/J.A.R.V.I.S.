import pyttsx3
import random
import datetime
import time
import webbrowser
import os
import smtplib
import subprocess
import wolframalpha
import wikipedia
import requests
import shutil
import pyaudio
import operator
import ctypes
from urllib.request import urlopen
from tkinter import *
converter = pyttsx3.init()
voice_id ="com.apple.speech.synthesis.voice.samantha"
converter.setProperty('voice', voice_id)
converter.setProperty('rate', 200)
converter.setProperty('volume', 1)
def speak(a):
    converter.say(a)
def byewish():
    arr3=["Have a nice day boss !","I hope i was usefull","I had a great time boss !","Hope to see you soon !","Always there for you boss !","Feel sad to see you go... see you soon boss !"]
    askkk=random.choice(arr3)
    txt.insert(END, '\n' + "FRIDAY ->  " +askkk)
    speak(askkk)
    converter.runAndWait()
def wishMe():
    arr4=["Good Morning sir! what can i do for you?","What a pleasant day ! how can i help you ?","Morning boss! What is my first task of the day ?","Good to see you sir! How can i help you ?","A very Good morning sir! What can i do for you?","What a sunny day! how can i help you sir?","friday at your service boss!"]
    arr5=["Good afternoon boss ! how can i help you ?","Afternoon ! how can i help you ?","I am barely awake!!! , though i can perform some of your tasks","how is the day going sir!, how can i make it better for you?","Yes boss ! How can i help you?","friday at your service boss!"]
    arr6=["Good evening boss ! what can i do for you?","Had a long day? Don't worry i am here to help","I love sunsets, and following your orders","I think i need a beer... and some of your tasks to perform","Today was a tough day, though i am ready to follow your orders","friday at your service boss!"]
    arr04=random.choice(arr4)
    arr05=random.choice(arr5)
    arr06=random.choice(arr6)
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12:
        speak(arr04)
        converter.runAndWait()
         
    elif hour>= 12 and hour<16:
        speak(arr05)
        converter.runAndWait()
         
    else:
        speak(arr06)
        converter.runAndWait()

wishMe()
root = Tk()
root.title(".F.R.I.D.A.Y.")
def send():
    def Print(a):
        txt.insert(END, '\n' + "FRIDAY ->  " + a)
        speak(a)
        converter.runAndWait()
    arr2=["What else can i do for you boss !","Anything else boss !","What is my next order boss !","Waiting for your next order boss !","Is there anything else i can do for you boss ?"]
    arr2ask=random.choice(arr2)
    arr=["bye","goodbye","quit","exit","kill the program","that's all for today","no"] 
    arr22=["hi","hello","what's up","hey","hola"]
    arr11=["hi","hello","hey","hola","namaste","glad to see you boss"]
    askk=random.choice(arr11)
    arr33=["who are you","what is your name","intro","introduction","do i know you","recognize","recognized"]
    arr33ask=["I am Friday, your virtual assistant and your big fan.","My name is often taken with joy on weekends, yes it's Friday.","Hi boss, i am Friday.","Hey it's me, Friday.","It's your virtual assistant, Friday","Friday reporting boss"]
    ask33=random.choice(arr33ask)
    send = "You -> "+e.get()
    txt.insert(END, '\n'+send)
    user = e.get().lower()
    if any(x in user for x in arr22):
        Print(askk)
    elif 'namaste' in user:
        Print('namastee')
    elif any(x in user for x in arr33):
        Print(ask33)
    elif "google" in user:
        Print("Here you go to Google") 
        webbrowser.get('safari').open_new("www.google.com")
        Print(arr2ask)
    elif 'from wikipedia' in user:
        Print("Checking the wikipedia")
        user=user.replace("wikipedia","")
        result = wikipedia.summary(user, sentences=4)
        Print("According to wikipedia")
        Print(result)
        Print(arr2ask)
    elif 'youtube' in user:
        Print("Here you go to Youtube")
        webbrowser.get('safari').open_new("www.youtube.com")
        Print(arr2ask)
    elif 'time' in user:
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        if hour>=0 and hour<12:
            Print(f"Sir the time is {hour}:{minute}AM")

            
        if hour>=12:
            Print(f"Sir the time is {hour}:{minute}PM")

            
        Print(arr2ask)
        
        
    elif 'how are you' in user:
        Print("I am fine, Thank you")

        
        Print("How are you, Sir")

        
        

    elif 'fine' in user or "good" in user:
        Print("It's good to know that you are fine")

        
        Print(arr2ask)
        
        
    elif 'shut down' in user:
        speak("the system is going to shut down")
        
        subprocess.call(['osascript', '-e',
'tell app "System Events" to shut down'])
        os._exit(os.EX_OK)

    elif 'restart' in user:
        speak("the system is going to restart")
        
        subprocess.call(['osascript','-e','tell app "System Events" to restart'])
        os._exit(os.EX_OK)

    elif 'wifi' in user and 'on' in user:
        speak("Turning on the welifi")
        
        os.system("networksetup -setairportpower airport on")
        Print(arr2ask)
        

    elif 'wifi' in user and 'off' in user:
        speak("Turning off the welifi")
        
        os.system("networksetup -setairportpower airport off")
        Print(arr2ask)
        

    elif 'what can you do' in user:
        speak("Boss, as i am your virtual assistant")
        
        speak("I am programmed to follow your every instructions and fulfill your every order sincerely")
        
        speak("Besides, the domain of my capabilities are listed below...")
        
        Print("You can ask me to google anything or directly ask me to open the application.")

        
        Print("I can open youtube for you")

        
        Print("I have linkage with wikipedia too so you just have to ask me your doubts and i am here to resolve every single of them")
        
        
        Print("I can update you with time too")
        
        
        Print("To ease your workload , i can shut down your system and even make it restart")
        
        
        Print("I can even do your entertainment by opening Amazon Prime Video or Hotstar")
        
        
        Print("And i can open zoom video app for you too")
        
        
        Print("Last but not the least, i can even display your resonance study material at the resosir application")
        
        
        Print("Have a nice searching boss! and please tell me")
        
        Print(arr2ask)
        

    elif 'invented' in user:
        speak("I was invented by Mister Gaurav Srivastava, a genius who can flatter anyone by his good looks")
        
        Print(arr2ask)
        

    elif 'amazon prime' in user:
        speak("Opening Amazon Prime video")
        
        webbrowser.get('safari').open_new("https://www.primevideo.com/storefront/home/ref=atv_nb_logo")
        Print(arr2ask)
        

    elif 'hotstar' in user:
        speak("Opening Hotstar")
        
        webbrowser.get('safari').open_new("https://www.hotstar.com/in")
        Print(arr2ask)
        


    elif 'zoom' in user:
        speak("Opening Zoom Meeting right away")
        
        webbrowser.get('safari').open_new("https://us04web.zoom.us/join")
        Print(arr2ask)
        

    elif 'news' in user:
        speak("Got some fresh news for you sir!")
        
        webbrowser.get('safari').open_new("https://inshorts.com/en/read")
        Print(arr2ask)
        

    elif 'classroom' in user:
        speak("Shit... it's school time")
        
        webbrowser.get('safari').open_new("https://classroom.google.com/u/2/h")
        Print(arr2ask)
        

    elif 'resosir' in user:
        speak("Opening resosir boss")
        
        webbrowser.get('safari').open_new("https://resosir.com/app/learner")
        Print(arr2ask)
        
        
    elif any(x in user for x in arr):
        byewish()
        os._exit(os.EX_OK);

    else:
        Print("Sorry! I didn't got you")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()
