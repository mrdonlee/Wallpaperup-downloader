import random
import urllib.request
import requests
from bs4 import BeautifulSoup


def download(url):
    name = "wallpaper_sn" + str( random.randrange(1,10000) + random.randrange(1,10000) )
    full_name = name + ".jpg"
    urllib.request.urlretrieve(url, full_name)

def collector(pg):
    page = 1
    while page <= pg:
        url = 'http://www.wallpaperup.com/search/results/assassins+creed/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('img', {'class' : 'thumb'}):
            img = link.get('src')
            place_of_end = img.find('/thumb_')
            print(img)
            print( img[0:27] + img[35:44] + '/download/'+ img[57:place_of_end] )
            in_url = img[0:27] + img[35:44] + '/download/'+ img[57:place_of_end]
            download(in_url)
        page += 1


collector(1)
