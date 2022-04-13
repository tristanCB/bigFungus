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
# print(os.environ)
import pyodata
import requests
import json

class AcumaticaOdata():
    def __init__(self) -> None:
        self.COMPANY = 'Company'
        self.BASEENDPT = os.environ["ACUMATICAENDPT"]
        self.SERVICE_URL = f'{self.BASEENDPT}/odatav4/{self.COMPANY}/'
        self.GETFILE = f"{self.BASEENDPT}/Frames/GetFile.ashx?fileID="
    
    def getImageFromFileId(self):
        
        pass
    
    def get(self, endpt= "CSAnswers"):
        r=requests.get(self.SERVICE_URL+endpt, auth=('admin', os.environ["ACUMATICAPWD"]), verify=False)
        assert (r.status_code == 200)
        return r.json()['value']
    
    def getInvFiles(self):
        return self.get(endpt="File?$filter=PrimaryScreenID eq 'IN2025PL'")
    
    def getStockItems(self):
        return self.get(endpt="InventoryItem")

    def getInvCDfromName(self, string : str) -> str:
        return string.split("(")[1].split(")")[0]

    def getItemWithAttributes(self):
        attributes = self.get()
        files = self.getInvFiles()
        items = self.getStockItems()
        stockItems = {}
        
        for item in  items:
            itemAttributes = {}
            for atrib in attributes:
                if item['NoteID'] == atrib['RefNoteID']:
                    itemAttributes[atrib['AttributeID']] = atrib['Value']
            for file in files:
                if self.getInvCDfromName(file['Name']) == item['InventoryCD']:
                    itemAttributes["FileID"] = file['FileID']
                    pass                    
            stockItems[item["InventoryCD"]] = itemAttributes
            
        return stockItems

# pp.pprint(AcumaticaOdata().getStockItems())
# %%
# print('Stock Items (GYPSUM    )\\gypsum.jpg'
# %%
pp.pprint(AcumaticaOdata().getItemWithAttributes())

# pp.pprint(AcumaticaOdata().get(endpt="InventoryItem"))
# pp.pprint(AcumaticaOdata().getInvFiles())
# exit()
# stock = AcumaticaOdata().getItemWithAttributes()
# pp.pprint(stock)
exit()
# %%
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
        urlForGettingStock = acumaticaEndpoint + "/entity/Default/20.200.001/StockItem?$expand=Attributes"
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
