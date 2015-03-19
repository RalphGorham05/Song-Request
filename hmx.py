import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time
import json



class FormThread(threading.Thread):
    def __init__(self, delay, max_times, title, artist):
        threading.Thread.__init__(self)
        self.delay = delay
        self.max = max_times
        self.title = title
        self.artist = artist
        self.counter = []
        self.count = {}

    def run(self):
        t = 0
        while t < self.max:
            t += 1
            print 'Starting ' + self.name
            time.sleep(self.delay)
            filler(self.title, self.artist)
            print 'Ending ' + self.name + '\t' + str(t)
            self.counter.append(t)
            self.count[self.title] = self.counter[len(self.counter)-1]
            #print self.count



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


def run_threads():
    thread1 = FormThread(10,'Lie in Our Graves Live','Dave Matthews Band')
    #thread2 = FormThread(20, 'Gravity','John Mayer')
    #thread3 = FormThread(30, 'Aint It Fun','Paramore')
    #thread4 = FormThread(40, 'Hot for Teacher','Van Halen')


    thread1.start()
    #thread2.start()
    #thread3.start()
    #thread4.start()

    #thread1.join()
    #thread2.join()
    #thread3.join()
    #thread4.join()

    '''
    dmb = thread1.count
    mayer = thread2.count
    metallica = thread3.count
    misc = thread4.count

    all_bands = [dmb, mayer, metallica, misc]


    with open('counter.json', 'a') as f:
        json.dump(all_bands, f)


    '''
def tracker():
    data = []
    with open('counter.json') as read:
        data = json.load(read)

        for d in data:
            print d



def writer(title, count):
    with open('votes.txt', 'a') as w:
        w.write(title + '  ' + count)
        w.close()
       
def reader():
    with open('votes.txt', 'r') as f:
        for line in f:
            print line
        


#run_threads()
#writer()
 #reader()
