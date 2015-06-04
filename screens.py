import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class MainScreen(Screen):
    pass

class TextScreen(Screen):
    pass

class VoiceScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
