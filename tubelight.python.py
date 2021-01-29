#******************Import gridages*****************************************#

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
from tkinter import  *
from PIL import ImageTk ,Image
import tkinter as tk
import sys
import time
import calendar



#********************************************************#
engine = pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voice[0].id)

""" DICTIONARY PHRASES """
phrases = ["Phrase1", "Phrase2", "Phrase3"]




class Clock(tk.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tk.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%I:%M:%S %p')
        else:
            self.time     = time.strftime('%I:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()
        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S %p')
        else:
            new_time = time.strftime('%I:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)

 




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
                         


def func():
    greeting()
    speak("I am SASS.")
    while (1): 
        speak("How can I help you?")
        query=takeCommand().lower()
        if "goodbye" in query or "ok bye" in query or "stop" in query:
            speak('Good bye have a nice day!')
            print('Good bye.Have a nice day!')
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
            #   results=YoutubeSearch("search terms", max_results=20).to_dict()
            #   print(results)
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(20)
        #google
        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(20)
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
        #time
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
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
            time.sleep(20)
        
        elif "write a note" in query:
            speak("What should I write")
            note=takeCommand()
            file=open('demo.txt','w')
            speak("date include")
            # if 'yes' in snfm:
            #    file.write(note)
            # else:    
            file.write(note) 
        
        elif "note" in query:
            speak("showing notes")
            file=open('demo.txt',"r")
            print(file.read())
            speak(file.read(6)) 

        #shutdown
        elif "shutdown" in query:
            speak("Do you want to shutdown?")
            shut=takeCommand()
            if "yes" in shut:
                print("Shutting down computer")
                speak("Shutting down computer")
                os.system("shutdown /s /t 30")
           

           


if __name__=="__main__":
    #interface
    root=Tk()
    root.title('SAS')
    root.configure(bg='#BCD5E5')
    root.geometry('700x700')


    frameCnt = 30
    frames = [PhotoImage(file='giphy.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    
    def search():
        url=entry.get()
        webbrowser.open(url)
    #label1=Label(root,text="Enter URL here:",font=
                                   # ("arial",15,"bold"))
  
    entry=Entry(root,width=35) 
    
    btn=Button(root,text="Search",command=search,bg="pink",
                            fg="white",font=("arial",14,"bold"))
    
    
    
    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
    label = Label(root)

    root.after(0, update, 0)
    
    w = Label(root, text=f"{datetime.datetime.now():%a, %b %d %Y}", fg="black", font=("helvetica", 15))

   


    lspace3=Label(text="              ",bg='#BCD5E5')
    lspace3.grid(row=0,column=0)

    my_img1 = ImageTk.PhotoImage(Image.open("voice1.png"))
    cbutton = Button(root, image =my_img1 ,bg='#BCC6CE',padx=10,pady=10, command=lambda: func())
    
            
    


    img1 = ImageTk.PhotoImage(Image.open("note.png"))
    buttonscratch = Button(root, image = img1 ,command=lambda: os.startfile('demo.txt'))


    lspace3=Label(text="              ",bg='#BCD5E5')
    lspace4 = Label(text="              ",bg='#BCD5E5')
    lspace5 = Label(text="              ",bg='#BCD5E5')

       # this displays the clock know as clock1
    clock1 = Clock(root)


# This gives the clock format.
    clock1.configure(bg='white',fg='black',font=("helvetica",15))

    



    
    


    #positions
    label.grid(row=0,column=1)
    lspace3.grid(row=1,column=1)
    lspace4.grid(row=5,column=1)
    lspace5.grid(row=7,column=0)
    cbutton.grid(column=1, row=2)
    buttonscratch.grid(row=8,column=0)
    #label1.grid(row=5,column=0)
    entry.grid(row=6,column=1)
    btn.grid(row=8,column=1)
    w.grid(row=8,column=2)
    clock1.grid(row=9,column=2)




    root.mainloop()
    