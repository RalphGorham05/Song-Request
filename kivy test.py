__author__ = 'Jarrod'

import kivy
kivy.require('1.8.0') # replace with your current kivy version !



from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class FormInput(GridLayout):

    def __init__(self, **kwargs):
        super(FormInput, self).__init__(**kwargs)
        self.cols = 2
        self.row_force_default=True
        self.row_default_height=40
        self.add_widget(Label(text='Song Title',size_hint_x=1, width=50))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)
        self.add_widget(Label(text='Artist'))
        self.artist = TextInput(multiline=False)
        self.add_widget(self.artist)
        self.but = Button(text='Add more rows', font_size=14)
        #self.but.bind(on_press=self.tester)
        self.add_widget(self.but)
        self.but2 = Button(text='Run', font_size=14)
        self.but2.bind(on_press=self.run_threads)
        self.add_widget(self.but2)
        

    def run_threads(self, instance):
        print 'pressed'
        print self.title.text

    



class MyFormApp(App):

    def build(self):
        return FormInput()


if __name__ == '__main__':
    MyFormApp().run()
