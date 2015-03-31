import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup
import threading
import time
import json
import collections
from peewee import *
import pygame
from pygame import mixer_music, mixer



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
    db = MySQLDatabase('SongLog', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class Songs(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')



    db.connect()

    db.create_table(Songs)
    '''
    test = 'Twist and Shout'
    for song in SongCount.select():
        if song.name == test:
            print song.votes


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
    db = MySQLDatabase('SongLog', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class Songs(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')

    db.connect()

    s = Songs.create(name = title,votes = count)

    song_name = Songs.get(Songs.name == title).name

    #updates count for song that are already in table
    if song_name:
        update = Songs.update(votes = Songs.votes + int(count)).where(Songs.name == title)
        update.execute()




def play_music():
    #pygame.init()
    pygame.mixer.init()
    loc = 'C:\Users\Jarrod\Downloads\Fringe_Theme_FULL_125k.ogg'
    mixer.music.load(loc)
    mixer.music.play(-1)

    time.sleep(5)
    print 'done'


#track()
#run_threads()
#writer()
#reader()
#play_music()
