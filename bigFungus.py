# save this as app.py
from operator import index
from re import template
from flask import Flask, redirect, request
from flask import render_template, url_for, session
import os
import glob
# Payments https://stripe.com/docs/checkout/quickstart
import stripe
# This is your test secret API key.
stripe.api_key = '<my secret key>'

app = Flask(__name__)

# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     print("adding header")
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# https://docs.gunicorn.org/en/stable/deploy.html
# 


pages = ["shop", "about", "francais"]
# Theaming
logo_txt = 'big_fungus.png'
css = '/css/style.css'
print(f"css --> {css}")

# Units
assert css

@app.route('/')
@app.route('/shop')
def format(theme="Light", code=200):
    page = "shop"
    print(code)
    print(theme)
    distribution_ammounts = [1, 2, 3, 4, 5]
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
            "name":"Unicorn grow bag T4 X 100",
            "alt_name":"100 X heat tolerant plastic mushroom bags",
            "image_url": "/product_images/T4GrowBag.jpg",
            "price": 199.99,
            "price_code":"price_1KJrXXCzLXa9dokVOlH6E10g",
            "uom":"unit",
            "description": "Made in the USA and have .3 micron filter patches. 100 bags per unit.",

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
    
    return render_template(
        'index.html', 
        distribution_ammounts=distribution_ammounts, 
        products=products,
        css=css,
        splash=False,
        logo_txt=logo_txt,
        pages=pages,
    )

@app.route('/francais')
@app.route('/home/')
@app.route('/about')
def splash():
    # print('At Home with big fungus')
    pass
    return render_template(
        'home.html',
        logo_txt=logo_txt,
        pages=pages,
    )

@app.route('/add/<code>/<quantity>', methods=['POST'])
def add_product_to_cart(code = None, quantity = None):
    print(code, quantity)
    return redirect(url_for('format', page="shop"))

YOUR_DOMAIN = 'http://127.0.0.1:5000'
@app.route('/create-checkout-session/', methods=['POST'])
def create_checkout_session():
    cart = request.form
    print(cart)
    line_items = [
    ]
    for item in cart:
        line_items.append({
                'price':item,
                'quantity':cart[item]
            })

    checkout_session = stripe.checkout.Session.create(
        shipping_address_collection={
            'allowed_countries': ['CA'],
        },
         shipping_options=[
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
        ],
        line_items=line_items,
        mode='payment',
        success_url= YOUR_DOMAIN + '/shop',
        cancel_url= YOUR_DOMAIN + '/shop',
    )
    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem') #certificate and key files  // ssl_context=context
    app.run('127.0.0.1', port=8000, debug=True)
    # serve(app, host='0.0.0.0', port=5000, url_scheme='https')
