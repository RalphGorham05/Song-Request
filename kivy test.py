__author__ = 'Jarrod'


from hmx import FormThread, writer
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
        self.cols = 9
        self.row_force_default=True
        self.row_default_height=40
        self.add_widget(Label(text='Song Title',size_hint_x=1, width=50))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)
        self.add_widget(Label(text='Artist'))
        self.artist = TextInput(multiline=False)
        self.add_widget(self.artist)
        self.add_widget(Label(text='Delay',size_hint_x=1, width=50))
        self.delay = TextInput(multiline=False)
        self.add_widget(self.delay)
        self.add_widget(Label(text='Max requests',size_hint_x=1, width=50))
        self.max = TextInput(multiline=False)
        self.add_widget(self.max)
        
        self.start1 = Button(text='Start', font_size=40)
        self.start1.bind(on_press=self.run_thread1)
        self.add_widget(self.start1)


        ##############2nd row######################################

        self.add_widget(Label(text='Song Title',size_hint_x=1, width=50))
        self.title2 = TextInput(multiline=False)
        self.add_widget(self.title2)
        self.add_widget(Label(text='Artist'))
        self.artist2 = TextInput(multiline=False)
        self.add_widget(self.artist2)
        self.add_widget(Label(text='Delay',size_hint_x=1, width=50))
        self.delay2 = TextInput(multiline=False)
        self.add_widget(self.delay2)
        self.add_widget(Label(text='Max requests',size_hint_x=1, width=50))
        self.max2 = TextInput(multiline=False)
        self.add_widget(self.max2)

        self.start2 = Button(text='Start', font_size=40)
        self.start2.bind(on_press=self.run_thread2)
        self.add_widget(self.start2)


        ################3rd row########################################

        self.add_widget(Label(text='Song Title',size_hint_x=1, width=50))
        self.title3 = TextInput(multiline=False)
        self.add_widget(self.title3)
        self.add_widget(Label(text='Artist'))
        self.artist3 = TextInput(multiline=False)
        self.add_widget(self.artist3)
        self.add_widget(Label(text='Delay',size_hint_x=1, width=50))
        self.delay3 = TextInput(multiline=False)
        self.add_widget(self.delay3)
        self.add_widget(Label(text='Max requests',size_hint_x=1, width=50))
        self.max3 = TextInput(multiline=False)
        self.add_widget(self.max3)

        self.start3 = Button(text='Start', font_size=40)
        self.start3.bind(on_press=self.run_thread3)
        self.add_widget(self.start3)
        

    def run_thread1(self, instance):
        thread = FormThread(int(self.delay.text), int(self.max.text), self.title.text, self.artist.text)
        thread.start()
        writer(self.title.text, self.max.text)

    def run_thread2(self, instance):
        thread = FormThread(int(self.delay2.text), int(self.max2.text), self.title2.text, self.artist2.text)
        thread.start()
        writer(self.title2.text, self.max2.text)

    def run_thread3(self, instance):
        thread = FormThread(int(self.delay3.text), int(self.max3.text), self.title3.text, self.artist3.text)
        thread.start()
        writer(self.title3.text, self.max3.text)




class MyFormApp(App):

    def build(self):
        return FormInput()


if __name__ == '__main__':
    MyFormApp().run()
