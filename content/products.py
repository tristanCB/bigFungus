def getProducts():
    products = [
            {
                "name":"Tissue Culture",
                "alt_name":"Sterile mushroom tissue culture.",
                "price": 15.99,
                "price_code":"price_1KJrTLCzLXa9dokV5oMt4KJq",
                "uom":"unit",
                "image_url": "/product_images/tissueCulture.png",
                
                "image_url_desc": "/product_images/kingTransparent.png",

                "title_description": "Pure, Isolated Mycelium",
                "description": "Perfect for starting your very own grainspawn or liquid cultures.",
                "description2": "The Agar medium was made using a recipe similar to Sabouraud agar. Our propriatary blend of ingredients and high standard of clenliness while manufacturing plates provides you with a guaranteed start to exploring a vast array of new mushroom strains. All batches are tested for possible baterial contamination.",

            },
        
            {
                "name":"Spawn",
                "alt_name":"Organic Rye Berry Grain Spawn",
                "price": 25.99,
                "price_code":"",
                "uom":"unit",
                "image_url": "/product_images/grainSpawn.png",
                
                "image_url_desc": "/product_images/grainSpawnCrossSection.jpg",
                "title_description": "Organic Rye Grain Spawn",
                "description": "Perfect for inoculating your very own bulk substrate. 1L masonjar, 3/4 full, fully colonized and ready to use",
                "description2": "On the left a cross section of grain can be seen. Because thr Mycelium is burried deep inside the grains, It can be broken vigurously and evenly mixed in bulk substrate for faster colonization.",

            },
        
            {
                "name":"Grow Kit",
                "alt_name":"Ready to fruit, fully colonized bulk substrate",
                "price": 39.99,
                "price_code":"price_1KJrOtCzLXa9dokVAfHJkTc3",
                "uom": "unit",
                "image_url": "/product_images/5lbsColonized.png",
                
                "image_url_desc": "/product_images/blackOysters.png",
                "title_description": "Ready To Fruit Fully Colonized",
                "description": "Includes one fully colonized artificial log grown in sterile mushroom grow bag. Can expect to get first harvest after keeping in humid environment for approximatly two weeks.",
                "description2": "One the left a block of black oysters can be seen emerging from the block. The plastic top was cut off,the block was then kept in a humid environment exposed to some light.",

            },

            {
                "name":"Unicorn grow bag",
                "alt_name":"100 X heat tolerant plastic mushroom bags",
                "image_url": "/product_images/T4GrowBag.jpg",
                "price": 199.99,
                "price_code":"price_1KJrXXCzLXa9dokVOlH6E10g",
                "uom":"unit",
                "description": "Model T4. Comes in bundle of 100. Made in the USA and have .3 micron filter patches. 100 bags per unit.",

            },
            {
                "name":"Liquid Culture",
                "alt_name":'Mycelial Suspension',
                "uom":"unit",
                "image_url": "/product_images/liquidCulture.png",
                "title_description": "Syringe Filled With Mycelium",
                "description": "Encapsulated mycelium in a propreatary suspension for effective use of injection ported bags.",
                "description2": "All Solutions are made using ISO9001 standards.",

            },
            {
                "name":"Parafilm",
                "alt_name":'Parafin thin film. 2" wide',
                "uom":"unit",
                "image_url": "/product_images/paraFilm.jpg",
                "description": "Includes all in one spore syringe, and sterilized media bag with injection port.",

            },
            {
                "name":"Seminar",
                "alt_name":'1hr live, personalized seminar on biology and practical home growing.',
                "uom":"unit",
                "image_url": "/product_images/seminar.png",
                "description": "Will contact to schedule time.",

            }
    ]
    return products

def getMycoNetBuilds() -> dict: 
    teks = {
        "PF Tek" : {
            "affiliateItems": [
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B0000BYCFU/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0000BYCFU&linkCode=as2&tag=bigfungus-20&linkId=91b53cc5b92863592fe9fe366458efd6"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B0000BYCFU&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07MZF9J2G/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07MZF9J2G&linkCode=as2&tag=bigfungus-20&linkId=60d2df268ab5871defea2d4f32c91a42"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07MZF9J2G&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',                
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07N7PSQM1/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07N7PSQM1&linkCode=as2&tag=bigfungus-20&linkId=9ff5a81e190df74b37553b119a02206d"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07N7PSQM1&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B00PG8RT6O/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00PG8RT6O&linkCode=as2&tag=bigfungus-20&linkId=b9d2b97c0976c9e06029b1eeed404295"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B00PG8RT6O&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B07J49CD76/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B07J49CD76&linkCode=as2&tag=bigfungus-20&linkId=c5ac9d11b317e539cbe5bddc26c7634e"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B07J49CD76&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>',
                '<a target="_blank"  href="https://www.amazon.com/gp/product/B000W7NNKA/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B000W7NNKA&linkCode=as2&tag=bigfungus-20&linkId=9019181d34abbbd61bf31f4364d5b151"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=B000W7NNKA&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=bigfungus-20" ></a>'
            ],
            "desc": "PF tek is a common and simple method for beginers. It involves using a spore syringe to innoculate pasterized or sterilized substarte made from vermiculite and brown rice flour. If you are just starting or like to keep things simple, this tek is what you are looking for.",
            "steps": [
                "Mix 450ml of water with 450g of vermiculite in a bowl",
                "Coat Vermiculite evenly with 250g of brown rice flour",
                "Loosely fill mason jars to leave approximatly 1cm of head space in each",
                "Wide 1cm rim clean of any water or debrit using a paper towel",
                "Top mason jar off with dry vermiculite",
                "drill 4 small holes in lids of jars, and tape them over with the millipore tape, cover full mason jar with taped lid, rim and a sheet of aluminium foil",
                "Line bottom of pressure cooker or cauldron with mason jar rims in order to prop the mason jar off the bottom during sterilization or pasterization",
                "Fill the bottom of the pressure cooker up with water (Follow the manufacturers instructions) and load the filled mason jar up",
                "Close pressure cooker, bring it up to pressure and allow for 1hour to pass",
                "Empty pressure cooker and let the jars cool down in a relatively clean place (Inside your stove while it is off)",
                "Procure liquid mycelium syringe or spore syringe from bigfungus.ca or other source"
            ],
            "website": "bigfungus",
            "item_type": "Tek (Technique)",
            "price":"~ 250 $",
            "img_href": "teks/pftek.png",
            "shortDesc": "Psilocybe fanaticus technique",
            "level": "Beginner"
        }
        
    }
    return teks

def getShippingOptionsStripe():
    ship = [
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 0,
                    'currency': 'cad',
                },
                'display_name': 'Free shipping',
                # Delivers between 5-7 business days
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 5,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 7,
                    },
                }
                }
            },
            {
                'shipping_rate_data': {
                'type': 'fixed_amount',
                'fixed_amount': {
                    'amount': 1500,
                    'currency': 'cad',
                },
                'display_name': 'Next day air',
                # Delivers in exactly 1 business day
                'delivery_estimate': {
                    'minimum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                    'maximum': {
                    'unit': 'business_day',
                    'value': 1,
                    },
                }
                }
            },
        ]
    return ship

def getComment():
    comments = [
        {
            "comment":"This is my first time purchaing, overall very satisfying process from start to finish. Very professional",
        },
        {
            "comment":"This is my second time purchaing, overall very satisfying process from start to finish. Very professional",
        }
    ]
    return comments