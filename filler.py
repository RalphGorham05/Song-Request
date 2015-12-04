from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Browser:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def goTo(self,url):
        self.browser.get(url)
    

def filler(title, artist, times = 1):
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

    t = 1
    while(t <times):
        filler(title, artist)
        t += 1


song = raw_input('Enter song title: ')
singer = raw_input('Enter artist: ')
votes = input('Enter amount of votes: ')

#filler(song,singer,votes)

br = Browser()
site = 'www.digg.com'
br.goTo(site)
