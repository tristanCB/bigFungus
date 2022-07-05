# %%
from ast import excepthandler
from pyparsing import NotAny
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
db.create_all()



def add_recipe(recipie):
    try:
        recep = model.Recipes(
                                  date_scrapped= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                , rating = 0
                                , title=recipie['title']
                                , website=recipie['website']
                                , img_href=recipie['img_href']
                                , link=recipie['link']
                            )
        db.session.add(recep)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(e)
        return False

def scrape_a_food_network_page(pageNum):
    # baseUrl = "https://www.allrecipes.com/element-api/content-proxy/faceted-searches-load-more?search=mushroom&page=3"
    baseUrl = f"https://www.foodnetwork.com/search/mushroom-/p/{pageNum}"
    website = "foodnetwork"
    soup = BeautifulSoup(requests.get(baseUrl).content, "html.parser")
    # pp.pprint(soup)

    tiles = soup.find_all(
        lambda tag:tag.name == "section" and
        "class" in tag.attrs and
        "o-RecipeResult" in tag.attrs["class"] and 
        "o-ResultCard" in tag.attrs["class"]
    )

    tile: bs4.element.Tag
    for tile in tiles:
        print(type(tile))
        # raise NotAny
        title = tile.select_one("span").get_text()
        link = tile.select_one("h3").select_one("a").attrs["href"]
        try:
            img_href = tile.select_one("img").attrs["src"]
        except AttributeError as e:
            print(e)
            img_href = str()
        recipe = {
            "title": title,
            "website": website,
            "img_href":img_href,
            "link":link, 
        }
        pp.pprint(recipe)
        add_recipe(recipe)
    
def mycelialCooker():
    i = 0
    while True:
        pageNum = i
        i += 1
        yield scrape_a_food_network_page(pageNum)
    yield

def crawl():
    gen = mycelialCooker()
    while True:
        next(gen)
        
crawl()
# def getitems(url):
#     soup = BeautifulSoup(requests.get(url).content, "html.parser")
#     claves = []
#     tile = soup.find_all(
#         lambda tag:tag.name == "div" and
#         "data-listing-id" in tag.attrs
#     )
#     # pp.pprint(claves)
#     for i in tile:
#         price = i.select_one(".price").get_text().strip().replace(u'\xa0', u' ')
#         img = i.select_one("img")
#         if 'data-src' in img.attrs:
#             img_href = img.attrs['data-src']
#         else:
#             img_href = img.attrs['src']
#         img_alt = img.attrs['alt']
#         link = baseUrl + i.select_one(".title").select_one("a").attrs['href']
#         item = {
#             "price":clean_price(price), 
#             "img_href":img_href, 
#             "img_alt":img_alt,
#             "link":link
#             }
#         claves.append(item)
#         pp.pprint(item)
#     return claves

# for keyword in keywords:
#     def craw_ebay():
#         for i in range(1,2):
#             url_at = f"https://www.ebay.ca/sch/i.html?_from=R40&_nkw={keyword}&_sacat=0&_pgn={i}"
#             soup = BeautifulSoup(requests.get(url_at).content, "html.parser")
#             tiles = soup.find_all("div", {"class": "s-item__wrapper clearfix"})

#             # pp.pprint(tiles)
#             for tile in tiles:
#                 # pp.pprint(tile)
#                 try:
#                     link= tile.select_one("a").attrs['href']
#                     price = tile.find("span", attrs={"class":"s-item__price"}).text
#                     img_alt = tile.find("h3", attrs={"class":"s-item__title"}).text
#                     img_href = tile.find("img", attrs={"class":"s-item__image-img"})["src"]

#                     item = {
#                         "price":clean_price(price), 
#                         "img_href":img_href, 
#                         "img_alt":img_alt,
#                         "link":link
#                         }
#                     if img_alt == 'Shop on eBay': continue
#                     add_clave(item, item_type=keyword)
#                     print(item)
#                 except Exception as e:
#                     print(e)

#     # %%
#     def generateClaves():
#         i = 0
#         while i < 2:
#             if i == 0:
#                 endpoint = f"{baseUrl}/b-quebec/{keyword}/k0l9001?rb=true&dc=true"
#             else:
#                 endpoint = f"{baseUrl}/b-quebec/{keyword}/page-{i}/k0l9001?rb=true&dc=true"
#             i += 1
#             claves = getitems(endpoint)
#             for z in claves:
#                 yield add_clave(z, item_type=keyword)
#         yield

#     def crawl_url_generated():
#         gen = generateClaves()
#         while True:
#             next(gen)

#     craw_ebay()
#     try:
#         crawl_url_generated()
#     except StopIteration:
#         continue    
