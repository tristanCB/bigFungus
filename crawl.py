# %%
import requests
import bs4
from bs4 import BeautifulSoup
import pprint
import re
pp = pprint.PrettyPrinter(indent=4)
from flask_sqlalchemy import SQLAlchemy
from bigFungusWeb import db, keywords
import os
import model 
import datetime
import re
import statistics
import typing
db.create_all()
# %%
def clean_price(stringPrice):
    print(stringPrice)
    
    def unclean_string_to_float(stringPrice):
        noLetters = re.sub("[^0-9]", '', stringPrice)
        if '' == noLetters: return 0
        price = float(noLetters[:-2])
        
        return price
    
    return statistics.mean(unclean_string_to_float(i) for i in stringPrice.split("to"))
    

def add_clave(item, website : str, item_type="Steam Sterilizer", ):
    try:
        clave = model.Autocalves(website=website, item_type=item_type,rating=0, date_scrapped= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),price=item['price'], img_href=item['img_href'], img_alt=item['img_alt'], link=item['link'])
        db.session.add(clave)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(e)
        return False
        
baseUrl = "https://www.kijiji.ca"

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
            "price":clean_price(price), 
            "img_href":img_href, 
            "img_alt":img_alt,
            "link":link
            }
        claves.append(item)
        pp.pprint(item)
    return claves

for keyword in keywords:
    def craw_ebay():
        for i in range(1,2):
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
                        "price":clean_price(price), 
                        "img_href":img_href, 
                        "img_alt":img_alt,
                        "link":link
                        }
                    if img_alt == 'Shop on eBay': continue
                    add_clave(item, website="ebay", item_type=keyword)
                    print(item)
                except Exception as e:
                    print(e)

    # %%
    def generateClaves():
        i = 0
        while i < 2:
            if i == 0:
                endpoint = f"{baseUrl}/b-quebec/{keyword}/k0l9001?rb=true&dc=true"
            else:
                endpoint = f"{baseUrl}/b-quebec/{keyword}/page-{i}/k0l9001?rb=true&dc=true"
            i += 1
            claves = getitems(endpoint)
            for z in claves:
                yield add_clave(z, website="kijiji", item_type=keyword)
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
