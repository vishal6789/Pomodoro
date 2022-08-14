from unicodedata import name
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

kv = Builder.load_file("application.kv")


class MainWindow(Widget):
    pass


class myApp(App):

    def build(self):
        return MainWindow()

if __name__ == "__main__":
    myApp().run()         