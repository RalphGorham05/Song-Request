import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time
import json



class FormThread(threading.Thread):
    def __init__(self, name, title, artist):
        threading.Thread.__init__(self)
        self.name = name
        self.title = title
        self.artist = artist
        self.counter = []
        self.count = {}

    def run(self,delay):
        t = 0
        while t < 10:
            t += 1
            print 'Starting ' + self.name
            time.sleep(delay)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.counter.append(t)
            self.count[self.title] = self.counter[len(self.counter)-1]
            #print self.count



class DMBThread(FormThread, threading.Thread):
    def __init__(self, name, title, artist):
        FormThread.__init__(self, name, title, artist) 
        threading.Thread.__init__(self)
        self.counter = []
        self.count = {}
        

    def run(self):
        delay = 30
        FormThread.run(self, delay)
        
        


class MayerThread(FormThread, threading.Thread):
    def __init__(self, name, title, artist):
        FormThread.__init__(self, name, title, artist) 
        threading.Thread.__init__(self)
        self.counter = []
        self.count = {}

    def run(self):
        delay = 40
        FormThread.run(self, delay)


class MetallicaThread(FormThread, threading.Thread):
    def __init__(self, name, title, artist):
        FormThread.__init__(self, name, title, artist) 
        threading.Thread.__init__(self)
        self.counter = []
        self.count = {}

    def run(self):
        delay = 50
        FormThread.run(self, delay)


class MiscThread(FormThread, threading.Thread):
    def __init__(self, name, title, artist):
        FormThread.__init__(self, name, title, artist) 
        threading.Thread.__init__(self)
        self.counter = []
        self.count = {}

    def run(self):
        delay = 60
        FormThread.run(self, delay)


def filler(title, artist):
    br = Browser()
    url = 'http://harmonixmusic.com/games/rock-band/request/'
    html = br.open(url)
    br.select_form(nr = 0)
    br.form['title'] = title
    br.form['artist'] = artist
    response = br.submit()

    content = response.read()
    soup = BeautifulSoup(content)
    p = soup.find('p').text
    print ''
    print p + ' ' +  title
    print ' '

# Create new threads
thread1 = DMBThread("DMB",'One Sweet World','Dave Matthews Band')
thread2 = MayerThread("Mayer", 'Where the Light Is','John Mayer')
thread3 = MetallicaThread("Metallica", 'Master of Puppets','Metallica')
thread4 = MiscThread("Miscellaneous", 'amor a la mexicana','thalia')


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

dmb = thread1.count
mayer = thread2.count
metallica = thread3.count
misc = thread4.count


with open('my_dict.json', 'a') as f:
    json.dump(dmb, f)
    json.dump(mayer, f)
    json.dump(metallica, f)
    json.dump(misc, f)

