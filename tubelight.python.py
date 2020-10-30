#******************Import Packages*****************************************#

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import wolframalpha
import json
import requests
from pycricbuzz import Cricbuzz
import time
import webbrowser
from youtube_search import YoutubeSearch


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
    while (1): 
        greeting()
        speak("Tell me how can I help you?")
        query=takeCommand().lower()
        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('Good bye')
            print('Good bye')
            break
    
           
      #wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("accordingly")   
            print(results)
            speak(results) 
        #youtube  
        elif 'open youtube' in query:
            #   results=YoutubeSearch("search terms", max_results=10).to_dict()
            #   print(results)
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(10)
        #google
        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(10)
        #gmail
        elif 'open mail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        #cricket score
        elif 'score' in query:
            c=Cricbuzz()

            matches=c.matches()
            for match in matches:
                print(match)
                #print(c.livescore(match['id']))
                print(c.scorecard(match['id']))
                break    
      #music
        if 'play music' in query:
            music_dir='C:\\Users\\HP\\Music'
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
      #weather
        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] -273
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in degree celsius is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in degree celsius = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
        #news
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(10)
        
        elif "write a note" in query:
            speak("What should I write")
            note=takeCommand()
            file=open('sammmy.txt','w')
            speak("date include")
            # if 'yes' in snfm:
            #    file.write(note)
            # else:    
            file.write(note) 
        
        elif "note" in query:
            speak("showing notes")
            file=open('sammmy.txt',"r")
            print(file.read())
            speak(file.read(6)) 
            
