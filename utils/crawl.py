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
import selenium
from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Tristan\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

db.create_all()
NUMBEROFPAGESTOSCRAPE = 1
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


def get_items_ebay(keyword, page):
    url_at = f"https://www.ebay.ca/sch/i.html?_from=R40&_nkw={keyword}&_sacat=0&_pgn={page}"
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

def get_items_kijiji(keyword, page):
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
    
    baseUrl = "https://www.kijiji.ca"
    if page == 0:
        endpoint = f"{baseUrl}/b-quebec/{keyword}/k0l9001?rb=true&dc=true"
    else:
        endpoint = f"{baseUrl}/b-quebec/{keyword}/page-{page}/k0l9001?rb=true&dc=true"
    claves = getitems(endpoint)
    for z in claves:
        add_clave(z, website="kijiji", item_type=keyword)

def get_items_amazon(keyword : str, page : int):
    baseUrl = "https://www.amazon.ca/s?k="
    def getItems(search = f"/s?k={keyword}&page={page}"):
        driver.get(baseUrl+search)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        tiles = soup.find_all(
            lambda tag:tag.name == "div" and
            "data-asin" in tag.attrs and
            "data-index" in tag.attrs and
            "data-uuid" in tag.attrs and 
            "data-component-id" in tag.attrs
        )
        # pp.pprint(soup)
        return tiles

    # pp.pprint(getItems())
    for tile in getItems():
        try:
            img_href = tile.select_one("img").attrs['src']
            title : bs4.element.Tag 
            title = tile.select_one("h2")
            img_alt = title.text
            price = tile.find(
                    lambda tag:tag.name == "span" and
                    "class" in tag.attrs and
                    "a-price-whole" in tag.attrs["class"]
                )
            pp.pprint(price.text.strip(",."))
            link = tile.select_one("a")['href']
            item = {
                "price":int(price.text.strip(".").replace(",",'')), 
                "img_href":img_href, 
                "img_alt":img_alt,
                "link": "https://www.amazon.ca" + link
            }
            pp.pprint(item)
            add_clave(item, website="amazon", item_type=keyword)
        except Exception as e:
            print(e)
            # pp.pprint(tile)
            # raise AssertionError

def get_items_etsy(keyword : str, page : int):
    baseUrl = "https://www.etsy.com/ca/"
    
    def getItems(search = f"search?q={keyword}&page={page}"):
        
        soup = BeautifulSoup(requests.get(baseUrl+search).text, "html.parser")
        tiles = soup.find_all(
            lambda tag:tag.name == "a" and
            "data-listing-id" in tag.attrs and
            "data-logging-key" in tag.attrs and
            "href" in tag.attrs
        )
        # pp.pprint(soup)
        return tiles

    for tile in getItems():
        try:
            img = tile.select_one("img")
            img_href = img.attrs['src']
            img_alt = img.attrs['alt']
            price = tile.find(
                lambda tag:tag.name == "span" and
                "class" in tag.attrs and
                "currency-value" in tag.attrs["class"]
            ).text
            link = tile["href"]
            item = {
                "price":clean_price(price), 
                "img_href":img_href, 
                "img_alt": img_alt,
                "link": link
            }

            pp.pprint(item)
            add_clave(item, website="etsy", item_type=keyword)
        except Exception as e:
            print(e)
            # pp.pprint(tile)
            raise AssertionError

if __name__ == "__main__":
    ## Crawl Websites
    for i in keywords:
        for j in range(0, NUMBEROFPAGESTOSCRAPE):
            get_items_kijiji(i, j)
            get_items_etsy(i, j)
            get_items_amazon(i, j)
            get_items_ebay(i, j)
