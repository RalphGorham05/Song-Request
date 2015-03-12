import mechanize
from mechanize import Browser
from bs4 import BeautifulSoup

br = Browser()
url = 'http://harmonixmusic.com/games/rock-band/request/'
html = br.open(url)
br.select_form(nr = 0)
br.form['title'] = 'Unforgiven'
br.form['artist'] = 'Metallica'
response = br.submit()

content = response.read()
soup = BeautifulSoup(content)
p = soup.find('p').text
print p


