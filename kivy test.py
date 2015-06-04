__author__ = 'Jarrod'

import kivy
kivy.require('1.8.0') # replace with your current kivy version !



from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import kivy_hmx
from kivy_hmx import FormApp


class Options(GridLayout):

    def __init__(self, **kwargs):
        super(Options, self).__init__(**kwargs)
        self.cols = 2
        self.row_force_default=True
        self.row_default_height=40

        self.textlb = Label(text = 'Hit Text to enter 3 different requests with text', font_size = 15)
        self.add_widget(self.textlb)
        
        self.but = Button(text='Text', font_size=14)
        
        self.but.bind(on_press=FormApp)
        self.add_widget(self.but)

        self.voicelb = Label(text = 'Hit Voice to enter request with voice', font_size = 15)
        self.add_widget(self.voicelb)
        self.but2 = Button(text='Voice', font_size=14)
        self.but2.bind(on_press=self.run_threads)
        self.add_widget(self.but2)
        

    def run_threads(self, instance):
        print 'pressed'

class ChooseApp(App):

    def build(self):
        return Options()


if __name__ == '__main__':
    ChooseApp().run()




