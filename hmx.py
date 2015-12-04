import threading
import time
import csv
import pygame

from mechanize import Browser
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
#from peewee import *
from pygame import mixer

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    url = 'http://harmonixmusic.com/games/rock-band/request/'
    
    browser = webdriver.Firefox()
    browser.get(url)

    #Enter song title and artist
    inputTitle = browser.find_element_by_name("title")
    inputTitle.send_keys(title)

    inputArtist = browser.find_element_by_name('artist')
    inputArtist.send_keys(artist)

    time.sleep(2)#wait for browser

    #click submit button
    browser.find_element_by_xpath("//form[1]").submit()
    

    time.sleep(2)
    #click restart button - absolute xpath
    browser.find_element_by_xpath("/html/body/div/div/div[1]/div/a").click()


    '''
    #old Mechanize way -- shut down b/c of added button
    br = Browser()
     html = br.open(url)
    br.select_form(nr = 0)
    br.form['title'] = title
    br.form['artist'] = artist
    response = br.submit()

    content = response.read()
    soup = BeautifulSoup(content)
    
    p = soup.find('p')
    print ''
    print p + ' ' +  title
    print ' '
    '''
   
    

    


def writer():
    db = MySQLDatabase('SongLog', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class Songs(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')



    db.connect()


    last = Songs.select().order_by(Songs.id.desc()).get().id
    for song in Songs.select():
        if song.id == 1:
            song.id == 55
        song.save()

    '''
    test = 'Twist and Shout'
    for song in SongCount.select():
        if song.name == test:
            print song.votes


    test = 'Two Step'
    if SongCount.get(SongCount.name == test).name:
        print SongCount.get(SongCount.name == test).votes
    '''
       



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


def excel():
    db = MySQLDatabase('SongLog', user='root', passwd='')

    class BaseModel(Model):
        class Meta():
            database = db


    class Songs(BaseModel):
        name = CharField(default='')
        votes = IntegerField(default='')



    db.connect()

    songs = []

    for song in Songs.select():
        songs.append((song.name, song.votes))


    with open('SongLog.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Song','Votes'))
        for song in songs:
            writer.writerow((song))


def reader(title, count):
    with open('SongLog.csv', 'r') as f:
        read = csv.reader(f)
        next(read, None)
        for row in read:
            old = int(row[1])
            if row[0] == title:
                old = old + count
                print old

def newTrack(title, count):
    with open('SongLog.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((title, count))





#track()
#run_threads()
#writer()
#reader('Grey Street',5)
#play_music()
#excel()
