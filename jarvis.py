import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
# voices=engine.getProperty("voices")
#
# engine.setProperty("voice",voices[0].id)
# print(voices[0].id)

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('tyagiujjawal763@gmail.com', 'my password')
        server.sendmail('tyagiujjawal763@gmail.com', to, content)
        server.close()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    # hour=int(datetime.datetime.now().hour)
    # if hour>=0 & hour<12:
    #     speak("gud morning")
    # elif hour>=12 & hour<18:
    #     speak("gud afternoon")
    # else:
    #     speak("gud evining")
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
                speak(f"Sir, the time is {strTime}")
            elif 'open code' in query:
                codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'email to ujjwal' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "ujjawal.tyagi.cse.2020@miet.ac.in"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend harry bhai. I am not able to send this email")
            elif 'stop' in query:
                exit()
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

# speak("hey ujjawal sir iam jarvish how may i help you")
wishme()
takeCommand()
