
import pyautogui
import pyttsx3
import speech_recognition as sr
#import webbrowser
import datetime
import wikipedia
import os
import pywhatkit
import pyjokes
import threading

import sys
from PyQt5 import QtGui
#from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisUI import Ui_Dialog


engine =pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)


def speak( audio):
    engine.say(audio)
    engine.runAndWait()

class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()
        speak("hello sir i am jarvis how may i help you")
        self.task_execution()

   # def run(self) :

    def command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold =1
            r.adjust_for_ambient_noise(source,duration=1)
            audio= r.listen(source)
        try:
            print("wait for few moments")
            self.query = r.recognize_google(audio,language='en-in')
            print(f"you just said :{self.query}\n")
        except Exception as e :
            print(e)
            speak("please tell me again")
            self.query ="none"
        return  self.query
    def wishings(self):
        hour= int(datetime.datetime.now().hour)
        if hour >=0 and hour <12 :
            print('good morning boss')
            speak('good morning boss')
        elif hour >=12 and hour <17 :
            print('good afternoon boss')
            speak('good afternoon boss')
        elif hour >= 17 and hour < 21:
            print('good evening boss')
            speak('good evening boss')
        else:
            print('good afternoon boss')
            speak('good afternoon boss')

    def task_execution(self):
        self.wishings()
        while True:
            self.query = self.command().lower()
            if 'time' in self.query :
                strTime =datetime.datetime.now().strftime("%H:%M:%S")
                speak("sir , the time is :"+ strTime)
                print(strTime)
            elif 'what can you do for me' in self.query:
                speak("as per my program i am bot which i can perform multiple task, through taking your voice as input commands")
            elif "minimize " in self.query:
                speak("minimizing sir ")
                pyautogui.hotkey('win','down','down')
            elif "maximise " in self.query or "maximize " in self.query:
                speak("maximize sir ")
                pyautogui.hotkey('win','up','up')
            elif "screenshot" in self.query:
                speak("taking screenshot sir..")
                pyautogui.hotkey('prtsc')
            elif " sir Thyagarajan " in self.query:
                speak("sir thyagarajan is a professer in nazareth collage of arts and sciene and also he is an head of department of computer application ")

            elif 'chrome' in self.query:
                speak("opening google chrome sir ")
                os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

                '''while True:
                    chromequery = self.command().lower()
                    if "search" in chromequery:
                        youtubequery=chromequery
                        youtubequery=youtubequery.replace("search","")
                        pyautogui.write(youtubequery)
                        pyautogui.press('enter')
                        speak('searching')

                    elif "close chrome" in chromequery or "exit chrome" in chromequery :
                        pyautogui.hotkey('ctrl','w')
                        speak("closing google chrome sir")
                        break'''

            elif 'wikipedia' in self.query:
                speak("searchnng in wikipedia ")

                try:
                    self.query= self.query.replace("wikipedia", "")
                    results= wikipedia.summary(self.query,sentences=1)
                    speak("according to wikipedia,")
                    print(results)
                    speak(results)
                    #break

                except:
                    speak("no results found..")
                    print("no results found..")

            elif 'play' in self.query:
                playQuery = self.query.replace("play","")
                speak("playing" + playQuery)
                pywhatkit.playonyt(playQuery)


            elif 'joke' in self.query:
                jarvisjoke = pyjokes.get_joke()
                print(jarvisjoke)
                speak(jarvisjoke)

            elif "quit" in self.query or "exit" in self.query:
                speak("i am leaving sir byee. have a nice day")
                quit()


class main(QTabWidget,QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.startpushButton.clicked.connect(self.starttask)
        self.ui.quitpushButton_2.clicked.connect(self.close)


    def starttask(self):
        # jarvis gif
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\heart.gif")
        self.ui.jarvisGIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        startexecution = Mainthread()




'''     # start label not button
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\start.png")
        self.ui.startlabelnotbutton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # quit label not button
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\exit.png")
        self.ui.quitlabelnotbutton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # earth gif
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\fa5c23af3f4cda50a9b49c4071ee4b55.gif")
        self.ui.globegif(self.ui.movie)
        self.ui.movie.start()
        #ironman background
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\irontemplate.webp")
        self.ui.ironmanGIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        # face gui
        self.ui.movie = QtGui.QMovie("C:\\Users\\aaa\\Downloads\\1_fhZsggnseKdBmY3_JonRkA.gif")
        self.ui.facegui(self.ui.movie)
        self.ui.movie.start()
        
'''


app = QApplication(sys.argv)
jarvis = main()
jarvis.show()

exit(app.exec_())

