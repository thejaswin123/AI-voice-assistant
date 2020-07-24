import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    day=int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back Sir")
    time()
    date()
    hour=int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<16:
        speak("good afternoon sir")
    elif hour>16 and hour<20:
        speak("good evening sir")
    else      :
        speak("good night sir")    
    speak("jarvis at your service please tell me how can i help you")
#wishme()   

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source, duration=1)
        #audio=r.listen(source)
        audio = r.listen(source=source, timeout=7, phrase_time_limit=6)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"        
    return query    

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("xyz@gmail.com","lmno")
    server.sendmail("xyz@gmail.com",to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("C:/Users/Welcome/Desktop/jarvis/ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    print("cpu is at" + usage)
    speak("cpu is at" + usage)
    battery=psutil.sensors_battery()
    print("battery is at " + str(battery.percent))
    speak("battery is at " + str(battery.percent))

def jokes():
    joke=pyjokes.get_joke()
    print(joke)
    speak(joke)

if __name__ == "__main__":
    #wishme()
    while True:
        query=takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()    
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i send?")
                content = takeCommand()
                to="abc@yahoo.in"
                speak(content)
                sendEmail(to,content)
                speak("Email has been successfully sent")
            except Exception as e:
                print(e)
                speak("unable to send email")   
        elif "search in chrome" in query:
            speak("what should i search for")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"    
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +'.com')            
        
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")  
        elif "play songs" in query:
            songs_dir="D:\\music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("what should i remember")
            data=takeCommand()
            speak("you said me to remember" +data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()    
        elif "do you want to tell me anything" in query:
            remember=open("data.txt","r")
            speak("you told me to remember" +remember.read())
        elif "screenshot" in query:
            screenshot()        
            speak("captured")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()              
        elif "offline" in query:
            quit()   
   