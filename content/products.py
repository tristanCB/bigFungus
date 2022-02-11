def getProducts():
    products = [
            {
                "name":"King Oyster Grow Kit",
                "alt_name":"Inoculated ans colonized substrate ready to fruit",
                "price": 39.99,
                "price_code":"price_1KJrOtCzLXa9dokVAfHJkTc3",
                "uom": "unit",
                "image_url": "/product_images/readyToFruit.jpg",
                "description": "Includes one fully colonized artificial log grown in sterile mushroom grow bag.",
            }, 

            {
                "name":"King Oyster Tissue Culture",
                "alt_name":"Sterile mushroom tissue culture.",
                "price": 15.99,
                "price_code":"price_1KJrTLCzLXa9dokV5oMt4KJq",
                "uom":"unit",
                "image_url": "/product_images/tissueCulture.jpg",
                "description": "Perfect for starting your very own cultures.",

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