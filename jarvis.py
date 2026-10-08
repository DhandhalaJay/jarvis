from turtle import listen
import speech_recognition as sr
import pyttsx3  # pip install pyttsx3
import datetime
import wikipedia # type: ignore #pip install wikipedia
import webbrowser
import os
import smtplib 


engine = pyttsx3.init('sapi5') # type: ignore
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<10:
        speak("Good Morning!")

    elif hour>=11 and hour<15:
        speak("Good Afternoon!")   

    elif hour>=15 and hour<20:
        speak("Good Evening!")  

    else:
        speak("Good Night!")
    speak("Hello! How can I assist you today?")
    speak("I am jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('j.k.paliwal07@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('j.k.paliwal07@gmail.com', 'your-password')
    server.sendmail('j.k.paliwal07@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open college' in query:
            webbrowser.open("https://www.ssccm.ac.in/")   


        elif 'play music' in query:
            webbrowser.open("https://www.spotify.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:/Users/jaydh/AppData/Local/Programs/Python/Python312/python.exe"
            os.startfile(codePath)
            
        elif 'how are you' in query:
            speak("I am fine, thank you.")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            
        elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak("Jarvis")

        elif "who i am" in query:
            speak("If you talk then definitely you're human.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by jaybhai")

        elif 'bye' in query:
                speak("bye sir, have a nice day")
                exit()
            
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

     else:
            speak("No query matched")
            print("No query matched")
        # print(e)
        # print("Say that again please...")
        # return "None"   
     print("No query matched")