import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time
import json




class DMBThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist
        self.count = []
        self.dict = {}

    def run(self):
        t = 0
        while t < 10:
            t += 1
            print 'Starting ' + self.name
            time.sleep(30)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.count.append(t)
            self.dict[self.title] = self.count[len(self.count)-1]
            #print self.dict


class MayerThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist
        self.count = []
        self.dict = {}

    def run(self):
        t = 0
        while t < 10:
            print 'Starting ' + self.name
            t += 1
            time.sleep(40)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.count.append(t)
            self.dict[self.title] = self.count[len(self.count)-1]

class MetallicaThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist
        self.count = []
        self.dict = {}

    def run(self):
        t = 0
        while t < 10:
            print 'Starting ' + self.name
            t += 1
            time.sleep(50)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.count.append(t)
            self.dict[self.title] = self.count[len(self.count)-1]

class MiscThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist
        self.count = []
        self.dict = {}

    def run(self):
        t = 0
        while t < 10:
            print 'Starting ' + self.name
            t += 1
            time.sleep(60)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.count.append(t)
            self.dict[self.title] = self.count[len(self.count)-1]


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
    print ' '
    print p + ' ' +  title
    print ' '

# Create new threads
thread1 = DMBThread(1, "DMB",'Dreamgirl','Dave Matthews Band')
thread2 = MayerThread(2, "Mayer", 'Gravity','John Mayer')
thread3 = MetallicaThread(3, "Metallica", 'Orion','Metallica')
thread4 = MiscThread(4, "Miscellaneous", 'Uptown Funk','Mark Ronson Bruno Mars')


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

dmb = thread1.dict
mayer = thread2.dict
metallica = thread3.dict
misc = thread4.dict


with open('my_dict.json', 'w') as f:
    json.dump(dmb, f)
    json.dump(mayer, f)
    json.dump(metallica, f)
    json.dump(misc, f)
