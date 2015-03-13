import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time


class DMBThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist

    def run(self):
        print 'Starting ' + self.name
        filler(self.title, self.artist)
        print 'Ending ' + self.name


class MayerThread(threading.Thread):
    def __init__(self, threadID, name, title, artist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.title = title
        self.artist = artist

    def run(self):
        print 'Starting ' + self.name
        time.sleep(5)
        filler(self.title, self.artist)
        print 'Ending ' + self.name


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
    print p + ' ' +  title

# Create new threads
thread1 = DMBThread(1, "DMB",'Grey Street','Dave Matthews Band')
thread2 = MayerThread(2, "Mayer", 'Gravity','John Mayer')

# Start new Threads
thread1.start()

thread2.start()

print 'Main thread over'