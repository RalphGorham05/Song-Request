import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time
import json
import collections
from peewee import *



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


def writer():
    db = MySQLDatabase('voteCount', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class SongCount(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')



    db.connect()

    test = 'Twist and Shout'
    for song in SongCount.select():
        if song.name == test:
            print song.votes

    '''
    test = 'Two Step'
    if SongCount.get(SongCount.name == test).name:
        print SongCount.get(SongCount.name == test).votes
    '''
       
def reader():
    newl = []
    with open('votes.txt', 'r') as f:
        for line in f:
            line = line.split()
            song = line[:len(line)-1]
            newl.append(song)
        print newl



def track(title, count):
    db = MySQLDatabase('voteCount', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class SongCount(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')

    db.connect()


    s = SongCount.create(name = title,votes = count)

    song_name = SongCount.get(SongCount.name == title).name

    #updates count for song that are already in table
    if song_name:
        update = SongCount.update(votes = SongCount.votes + int(count)).where(SongCount.name == title)
        update.execute()






#track()
#run_threads()
#writer()
#reader()
