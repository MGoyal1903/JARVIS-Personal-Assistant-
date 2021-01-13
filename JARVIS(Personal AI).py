#creator =====Mayank Goyal
#import all the dependencies
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit
import datetime
import webbrowser
import pyjokes
import os
import cv2
from requests import get
import sys
import pyautogui

#creator ====Mayank Goyal

#starting of jarvis
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
voices=engine.setProperty('voice',voices[0].id)
engine.say("Test voice to check is Jarvis is running correctly... ")
engine.runAndWait()


#creator ====Mayank Goyal

#create text to speak function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#creator ====Mayank Goyal

# jarvis take command to user 
def talkcommand():
    listen=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        listen.pause_threshold=1
        audio=listen.listen(source,timeout=10,phrase_time_limit=5)

    try:
        print("Recognization.....")
        query=listen.recognize_google(audio,language='en-in')   
        print(f"user said: {query}") 

    except Exception as e:
        speak("Say that again please")
        return None

    return query    


#creator ====Mayank Goyal

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>0 and hour<12:
        speak("Good Morning sir")

    elif hour>12 and hour<18:
        speak("Good afternoon sir")

    else:
        speak("Good Evening sir")

    speak(" My name is jarvis Please tell me how may i help you")    


#creator ====Mayank Goyal

#main function
if __name__ == "__main__":
    # speak("Hello Mayank") 
    # talkcommand()
       wishme()

while True:
        query=talkcommand().lower()

        #Building logic

        if 'notepad' in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cap.destroyAllWindows()  

        #Playing any song on youtube
        elif 'play' in query:
            song=query.replace('play','')
            speak('Playing..'+ song)
            pywhatkit.playonyt(song)  

        #find ip address
        elif 'ip address' in query:
            ip=get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")            

        #search anything on wiki

        elif 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentence=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        #current date and time 

        elif 'time' in query:
            time=datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current date and time is' + time)


        #open anything in webbrowser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir what should i search on google")
            cm=talkcommand.lower()
            webbrowser.open(f"{cm}") 

        #send whatsapp message
        elif 'send message' in query:
            pywhatkit.sendwhatmsg("+918383802148","Hello this side jarvis",12,47)   

         #jokes 
        elif 'joke' in query:
            speak(pyjokes.get_jokes())    


        #to close any application
        elif 'close notepad' in query:
            speak("okay sir closing notepad")
            os.system("taskkill / f /im notepad.exe ")


        #change windows tabs
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")    


        elif 'no thanks' in query:
            speak("Thanks for using me sir,have a good day")
            sys.exit()  



        speak("sir do you have any other work")    

 #creator ====Mayank Goyal 

###########################  END OF PROGRAM ############################# 