# %%
import requests
import bs4
from bs4 import BeautifulSoup
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)
from flask_sqlalchemy import SQLAlchemy
from bigFungus import db
import os
from bigFungus import Autocalves
import datetime

db.create_all()
# %%


def add_clave(item, item_type="Steam Sterilizer"):
    try:
        clave = Autocalves(item_type=item_type, date_scrapped= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),price=item['price'], img_href=item['img_href'], img_alt=item['img_alt'], link=item['link'])
        db.session.add(clave)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(e)
        return False
        
keywords = ["Steam Sterilizer", "impulse sealer", "Mushroom bag", "Mushroom"]
baseUrl = os.environ["URLSCRAPPED1"]

def getitems(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    claves = []
    tile = soup.find_all(
        lambda tag:tag.name == "div" and
        "data-listing-id" in tag.attrs
    )
    # pp.pprint(claves)
    for i in tile:
        price = i.select_one(".price").get_text().strip().replace(u'\xa0', u' ')
        img = i.select_one("img")
        if 'data-src' in img.attrs:
            img_href = img.attrs['data-src']
        else:
            img_href = img.attrs['src']
        img_alt = img.attrs['alt']
        link = baseUrl + i.select_one(".title").select_one("a").attrs['href']
        item = {
            "price":price, 
            "img_href":img_href, 
            "img_alt":img_alt,
            "link":link
            }
        claves.append(item)
        pp.pprint(item)
    return claves

for keyword in keywords:
    def craw_ebay():
        for i in range(10):
            url_at = f"https://www.ebay.ca/sch/i.html?_from=R40&_nkw={keyword}&_sacat=0&_pgn={i}"
            soup = BeautifulSoup(requests.get(url_at).content, "html.parser")
            tiles = soup.find_all("div", {"class": "s-item__wrapper clearfix"})

            # pp.pprint(tiles)
            for tile in tiles:
                # pp.pprint(tile)
                try:
                    link= tile.select_one("a").attrs['href']
                    price = tile.find("span", attrs={"class":"s-item__price"}).text
                    img_alt = tile.find("h3", attrs={"class":"s-item__title"}).text
                    img_href = tile.find("img", attrs={"class":"s-item__image-img"})["src"]

                    item = {
                        "price":price, 
                        "img_href":img_href, 
                        "img_alt":img_alt,
                        "link":link
                        }
                    add_clave(item, item_type=keyword)
                    print(item)
                except Exception as e:
                    print(e)

    # %%
    def generateClaves():
        i = 0
        while i < 5:
            if i == 0:
                endpoint = f"{baseUrl}/b-quebec/{keyword}/k0l9001?rb=true&dc=true"
            else:
                endpoint = f"{baseUrl}/b-quebec/{keyword}/page-{i}/k0l9001?rb=true&dc=true"
            i += 1
            claves = getitems(endpoint)
            for z in claves:
                yield add_clave(z, item_type=keyword)
        yield

    def crawl_url_generated():
        gen = generateClaves()
        while True:
            next(gen)

    craw_ebay()
    try:
        crawl_url_generated()
    except StopIteration:
        continue    
