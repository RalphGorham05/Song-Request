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
                'count': 0,
                'date': []
                }
        client = MongoClient()
        db = client.rock_band
        songs = db.songs
        test = db.test
        if test.find({'title': title}).count > 0:
            print 'already exists'
            test.update({'artist': artist, 'title': title},
                         {
                             '$inc': {'count': 1},
                             '$set': {'date': datetime.datetime.utcnow()}
                         }
                         )
        else:
            print 'created'
            test.insert(song)

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
            self.connect_db(song_title, artist)

        time.sleep(5)

v = Voter()
v.run_voter()
