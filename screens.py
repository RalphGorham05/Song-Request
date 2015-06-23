import kivy
kivy.require('1.8.0') # replace with your current kivy version !

#imports for Screens
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

#imports for FormInput(text option)
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from hmx import FormThread, newTrack

#from audioInput import AudioInput

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

        
        self.returnbutton = Button(text='Main Menu', font_size=15)
        self.returnbutton.bind()
        self.add_widget(self.returnbutton)
        

        #self.main_audio()
        

    def run_thread1(self, instance):
        thread = FormThread(int(self.delay.text), int(self.max.text), self.title.text, self.artist.text)
        thread.start()
        #thread.join()

        sound = SoundLoader.load('glass_ping.wav')
        sound.play()
        newTrack(self.title.text, self.max.text)

    def run_thread2(self, instance):
        thread = FormThread(int(self.delay2.text), int(self.max2.text), self.title2.text, self.artist2.text)
        thread.start()
        #thread.join()
        sound = SoundLoader.load('dj_scratching.wav')
        sound.play()
        newTrack(self.title2.text, self.max2.text)

    def run_thread3(self, instance):
        thread = FormThread(int(self.delay3.text), int(self.max3.text), self.title3.text, self.artist3.text)
        thread.start()
        thread.join()
        sound = SoundLoader.load('ufo_landing.wav')
        sound.play()
        newTrack(self.title3.text, self.max3.text)



class VoiceInput(GridLayout):
    def __init__(self, **kwargs):
        super(VoiceInput, self).__init__(**kwargs)
        #catch = AudioInput()
        self.cols = 8
        self.row_force_default=True
        self.row_default_height=40
        self.songbutton = Button(text='Song Name',size_hint_x=1, width=50)
        #self.songbutton.bind(on_press = catch.getSong())
        self.add_widget(self.songbutton)
        self.title= TextInput(text = 'song', multiline=False)
        self.add_widget(self.title)
        self.add_widget(Label(text='Artist'))
        self.artist = TextInput(multiline=False)
        self.add_widget(self.artist)
        self.add_widget(Label(text='Delay',size_hint_x=1, width=50))
        self.delay = TextInput(multiline=False)
        self.add_widget(self.delay)
        self.add_widget(Label(text='Votes',size_hint_x=1, width=50))
        self.max = TextInput(multiline=False)
        self.add_widget(self.max)





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
