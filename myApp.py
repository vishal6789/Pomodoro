from os import times_result
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


    #importing ObjectProperty
    PlayPause = ObjectProperty(None)
    DispTime = ObjectProperty(None)

    
    #defining required variables 
    TimerStarted = False
    TimerTime = 5 # seconds
    prompt = "Start"

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
        

    #Reset Button Clicked
    def reset_timer(self):
        
        self.TimerStarted = False
        self.TimerTime = 5 # 5 seconds
        self.prompt = "Start" 
        self.update_Disp()              
        Clock.unschedule(self.timer_count)

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
        self.ids.reset.text = "Time's UP"
        self.prompt = "Start"
        self.update_Disp()
        Clock.unschedule(self.timer_count)

    def update_Disp(self):
        mins,secs = self.TimerTime//60,self.TimerTime%60
        self.ids.DispTime.text = (str(int(mins))+':'+str(int(secs))+str(int(secs* 100 % 100)))
        self.ids.PlayPause.text = self.prompt


    pass


class myApp(App):
    
    #Setting application Tittle 
    App.title = "Pomodoro App"
    def build(self):
        return MainWindow()

if __name__ == "__main__":
    myApp().run()         