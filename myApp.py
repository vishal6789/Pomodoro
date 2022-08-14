from os import times_result
from sqlite3 import complete_statement
from unicodedata import name
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from time import strftime
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader


#Configuring Window size
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')

#Including .kv Design file
kv = Builder.load_file("application.kv")



class MainWindow(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_start()    


    #defining required variables 
    TimerStarted = False
    TimerTime = 5 # 25mins
    prompt = "Start"
    IsWork = True
    WorkCount = 1
    BreakCount = 0 
    l = {}
    
    #Timer Starts
    def on_start(self):
        Clock.schedule_interval(self.timer_count,0)
        

    #PlayPause Button Clicked 
    def play_pause(self):
        Clock.unschedule(self.timer_count)
        Clock.schedule_interval(self.timer_count,0)
        self.TimerStarted = bool(1-int(self.TimerStarted))
        self.prompt = 'Pause' if self.TimerStarted else 'Start'
        # self.PlayPause.text = self.prompt
        self.ids.PlayPause.text = self.prompt
        
        
        

    #Updating Counter 
    def timer_count(self,sleep):
        if self.TimerStarted:
            self.TimerTime -= sleep
        self.update_Disp()
        if self.TimerTime <= 0.10:
            self.time_complete()

    def time_complete(self):
        self.TimerStarted = False
        self.TimerTime = 0
        # self.ids.reset.text = "Time's UP"
        self.prompt = "Start"
        self.update_Disp()
        Clock.unschedule(self.timer_count)
        self.update_count()


    def update_Disp(self):
        mins,secs = self.TimerTime//60,self.TimerTime%60
        self.ids.DispTime.font_size = '40sp'
        self.ids.DispTime.text = (str(+int(mins))+':'+str(int(secs))+':'+str(int(secs* 100 % 100)))
        self.ids.PlayPause.text = self.prompt
        work = "WORK" if self.IsWork else "BREAK"
        self.ids.process.text = work


    def update_count(self):
        if self.IsWork:
            self.IsWork = False
            self.WorkCount += 1
            self.BreakCount += 1

            if self.BreakCount==1:
                self.ids.label1.color = 0,1,1,1

            elif self.BreakCount==2:
                self.ids.label2.color = 0,1,1,1
            
            elif self.BreakCount==3:
                self.ids.label3.color = 0,1,1,1
            
            elif self.BreakCount==4:
                self.ids.label4.color = 0,1,1,1


            if self.BreakCount%4==0:
                self.TimerTime = 8 #20 min long break
            else:
                self.TimerTime = 3 # 5 min short break

        else:
            self.IsWork = True
            if self.WorkCount==5:
                self.complete_reset()
            else:
                self.TimerTime = 5 #25 min work  
        print("Work:",self.WorkCount,"break",self.BreakCount)
        self.play_pause()
        self.update_Disp()
    
    def complete_reset(self):
        self.TimerStarted = bool(1-int(self.TimerStarted))
        self.TimerTime = 5 # 25mins
        self.prompt = "Start"
        self.IsWork = True
        self.WorkCount = 1
        self.BreakCount = 0 

        self.ids.label1.color = 1,1,1,1
        self.ids.label2.color = 1,1,1,1
        self.ids.label3.color = 1,1,1,1
        self.ids.label4.color = 1,1,1,1




        Clock.unschedule(self.timer_count)
        Clock.schedule_interval(self.timer_count,0)
        self.update_Disp()


    pass


class myApp(App):
    
    #Setting application Tittle 
    App.title = "Pomodoro App"
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    myApp().run()         