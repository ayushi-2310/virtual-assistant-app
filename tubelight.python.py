#******************Import Packages*****************************************#

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import wolframalpha

#********************************************************#
engine = pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voice[0].id)
#greeting
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greeting():
    hours=int(datetime.datetime.now().hour)
    if hours>=3 and hours<=12:
        speak("Good Morning")
    elif hours>12 and hours<=15:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        
        print("Listening....")
        r.adjust_for_ambient_noise(source,duration=1)
        print("now speak")
                   
        
        audio=r.listen(source)
       # print('happy')
        
    try:
        print('Recognising...')
        query = r.recognize_google(audio,language='en-in')
        print(f"You said:{query}\n")
        
        
    except Exception as e:
        print("Say again!")
        return "None"
    
    
    
    return query
                         
        
if __name__=="__main__":
    if (1): 
        greeting()
        speak("Tell me how can I help you?")
      #wikipedia
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("accordingly")   
            print(results)
            speak(results)   
      #music
        if 'play music' in query:
            music_dir='C:\\Users\\This PC\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))
      #caluculations
        elif 'calculate' in query:
            speak('I can answer to computational questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
      #location
        elif 'location' in query:
            speak('I can answer to  geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
