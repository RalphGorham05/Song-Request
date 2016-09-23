from selenium import webdriver
import time
import datetime
from pymongo import MongoClient


class Voter:
    def __init__(self):
        self.url = 'http://www.harmonixmusic.com/games/rock-band/request/'

    def load_site(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        return browser

    @staticmethod
    def complete_form(site, song, artist):
        site.find_element_by_id('id_title').send_keys(song)
        site.find_element_by_id('id_artist').send_keys(artist)
        site.find_element_by_css_selector('.button').click()

    @staticmethod
    def connect_db(title, artist):
        song = {'artist': artist,
                'title': title,
                'count': 1,
                'date': [datetime.datetime.utcnow()]
                }
        client = MongoClient()
        db = client.rock_band
        songs = db.songs
        if songs.find({'title': title}).count > 0:
            print 'already exists'
            db.rock_band.update({'artist': artist, 'title': title},
                                      {'$set': {'count': song['count'] + 1}}
                                      )

        else:
            songs.insert(song)
            print 'created'


    def run_voter(self):
        song_title = raw_input('What is the song name: ')
        artist = raw_input('Who is the artist: ')
        site = self.load_site()
        self.complete_form(site, song_title, artist)

        try:
            voted_already = site.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/p')
            if voted_already:
                print 'voted already'
        except Exception:
            print 'success'
            thanks_button = site.find_element_by_xpath('/html/body/div/div/div[1]/div/a')
            thanks_button.click()

        time.sleep(5)

v = Voter()
v.connect_db('let the flames begin', 'paramore')
