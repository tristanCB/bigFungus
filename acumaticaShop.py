#%% Python
# Copyright TCB

# Uses an acumatica stock item as a shop item in an e-commerce website
from lib2to3.pytree import convert
from aiohttp import request
from grpc import StatusCode
import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
import os
# This is your test secret API key.
print(os.environ)

acumaticaEndpoint = os.environ["ACUMATICAENDPT"]
acumaticaPWD = os.environ["ACUMATICAPWD"]

class acumaticaApi():
    creds = {
        "name" : "admin",
        "password" : acumaticaPWD,
        "company" : "Company",
        "branch" : "BigFungus",
        "locale" : "en-US"
    }    
    def getStockItem(self):
        urlForGettingStock = acumaticaEndpoint + "/entity/Default/20.200.001/StockItem"
        return requests.get(urlForGettingStock, cookies=self.login.cookies, headers=self.login.cookies)

    def __init__(self) -> None:
        self.login = requests.post(f'{acumaticaEndpoint}/entity/auth/login', self.creds)
        print(self.login)
        print(self.login.content)
        #assert self.login.status_code == StatusCode.OUT_OF_RANGE
        pass
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        #Exception handling here
        logout = requests.post(f'{acumaticaEndpoint}/entity/auth/logout', self.creds)
        #assert logout.status_code == StatusCode.OUT_OF_RANGE

# %%
from ast import literal_eval
import codecs
acumaticaAp = acumaticaApi()
with acumaticaAp as a:
    stockItems =  literal_eval(codecs.decode(a.getStockItem().content, 'UTF-8'))
pp.pprint(stockItems)
