#%% Python
# Copyright TCB

# Uses an acumatica stock item as a shop item in an e-commerce website
from lib2to3.pytree import convert
from tokenize import String
from unicodedata import decimal
from aiohttp import request
from grpc import StatusCode
import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
import mysql.connector
from mysql.connector import Error
import os
# This is your test secret API key.
# print(os.environ)
import pyodata
import requests
import json
import shutil

class prodDict():
    def __init__(self):
        self.name               = str()
        self.alt_name           = str()
        self.price              = 0.00
        self.price_code         = str()
        self.uom                = 'unit'
        self.image_url          = str()
        self.image_url_desc     = str()
        self.title_description  = str()
        self.description        = str()
        self.description2       = str()
        
    def __iter__(self):
        # For converting to dict:
        # https://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
        iters = dict((x,y) for x,y in self.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)
        for x,y in iters.items():
            yield x,y

class AcumaticaOdata():
    def __init__(self) -> None:
        self.COMPANY = 'Company'
        self.DBNAME = 'acumaticadb'
        self.BASEENDPT = os.environ["ACUMATICAENDPT"]
        self.SERVICE_URL = f'{self.BASEENDPT}/odatav4/{self.COMPANY}/'
        self.GETFILE = f"{self.BASEENDPT}/Frames/GetFile.ashx?fileID="
        try:
            self.DBENDPOINT = os.environ["DBENDPOINT"]
            self.DBPASS = os.environ["DBPASS"]

            self.connection = mysql.connector.connect(host = self.DBENDPOINT,
                                                database = self.DBNAME,
                                                user = self.DBPASS ,
                                                password = self.DBPASS)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)
        
    def getImageFromDatabase(self, fileName, fileId='b33c365a-0651-4889-af52-6d08249af45d'):
        mycursor = self.connection.cursor()
        mycursor.execute(f"SELECT * FROM uploadfilerevision where FileID = '{fileId}'")
        myresult = mycursor.fetchone()
        filePath = f"./static/product_images/{fileName}.png"
        #Save Image
        with open(filePath, "wb") as fh:
            fh.write(myresult[3])
        return filePath
    
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
    
    def buildProductFromAttributes(self, itemAttributes : dict):
        product = prodDict()
        oneToOneMapping = {
            'NAME':'name', 
            'ALTNAME':'alt_name',
            'PRICE':'price',
            'PRICECODE':'price_code',
            'UOM':'uom',
            'image_url':'image_url',
            'IMAGEURLDE':'image_url_desc',
            'TITLEDESC':'title_description',
            'SHORTDESC':'description',
            'DESCRIPTIO':'description2',
        }
        for key in oneToOneMapping:
            if key in itemAttributes:
                # print(key, oneToOneMapping[key])
                setattr(product, oneToOneMapping[key], itemAttributes[key])
        
        return dict(product)

    def getItemWithAttributes(self):
        attributes = self.get()
        files = self.getInvFiles()
        items = self.getStockItems()
        products = []
        stockItems = {}
        
        for item in items:
            itemAttributes = {}
            for atrib in attributes:
                if item['NoteID'] == atrib['RefNoteID']:
                    itemAttributes[atrib['AttributeID']] = atrib['Value']
            for file in files:
                if self.getInvCDfromName(file['Name']) == item['InventoryCD']:
                    itemAttributes["FileID"] = file['FileID']
                    itemAttributes["image_url"] = self.getImageFromDatabase(item['InventoryCD'], fileId= file['FileID'])
                    pass
            if itemAttributes != {}:
                stockItems[item["InventoryCD"]] = itemAttributes
                if itemAttributes['ISECOM'] == '1':
                    product = self.buildProductFromAttributes(itemAttributes)
                    products.append(product)
        return products
    
if __name__ == "__main__":
    pp.pprint(AcumaticaOdata().getItemWithAttributes())
