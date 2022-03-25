# save this as app.py
from binascii import Incomplete
from operator import index
from re import template
from flask import Flask, redirect, request, send_from_directory
from flask import render_template, url_for, session, stream_with_context
from flask import Response
# from flask.logging import 
from time import sleep
import datetime
# Local modules
# import content
from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery
from sqlalchemy.orm.attributes import flag_modified
import typing
import os
import glob
# Payments https://stripe.com/docs/checkout/quickstart
import stripe
import pprint
pp = pprint.PrettyPrinter(indent=2)
# DB interface
from content.products import getProducts
from content.techniques import getMycoNetBuilds
from content.indentification import getMycoNetIdentification
from content.shipping import getShippingOptionsStripe
from content.seo import getMeta, getPages

# import logging 

# This is your test secret API key.
stripe.api_key = os.environ["stripeApiKey"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://admin:{os.environ["pwd"]}@{os.environ["DBENDPOINT"]}/big-fungus-2'
db = SQLAlchemy(app)
db.create_all()

import model
# output_file_handler = logging.FileHandler("output.log")
# app.logger.addHandler(output_file_handler)

# @app.after_request
# def log(r):
#     log = model.Logger(date_accessed=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ip=request.remote_addr)
#     print(log)
#     db.session.add(log)
#     db.session.commit()
#     return r

keywords    = ["Steam Sterilizer", "Impulse sealer", "Mushroom bag", "Petri dish", "Isopropyl", "Hepa filter", "Humidifier"]

distribution_ammounts = [1, 2, 3, 4, 5]

# Theming
logo_txt = 'big_fungus.png'
css = '/css/style.css'
assert css

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/shop')
@app.route('/Shop')
def shop():    
    return render_template(
        'index.html', 
        distribution_ammounts=distribution_ammounts, 
        products=getProducts(),
        css=css,
        splash=False,
        logo_txt=logo_txt,
        pages=getPages(),
        seo=getMeta()
    )

@app.route('/Home')
@app.route('/About')
def splash():
    # print('At Home with big fungus')
    pass
    return render_template(
        'home.html',
        logo_txt=logo_txt,
        pages=getPages(),
        seo=getMeta()
    )

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # rv.enable_buffering(1)
    return rv

@app.route("/time/")
def time():
    def streamer():
        while True:
            yield str(datetime.datetime.now())
            sleep(1)
    return Response(streamer())

@app.route('/vote/<mycNet>/', methods=['POST'])
@app.route('/vote/<mycNet>/<itemType>', methods=['POST'])
def vote(mycNet = None, itemType=None):
    if request.method == 'POST':
        if "Equipment" in mycNet: 
            mod = model.Autocalves
        elif "Recipes" in mycNet: 
            mod = model.Recipes
        
        if "voteDown" in request.form:
            count =  mod.query.filter_by(id=str(request.form["voteDown"])).first()
            if count.rating is None: 
                count.rating = 0
            else:
                count.rating -= 1
                
        if "voteUp" in request.form:
            count =  mod.query.filter_by(id=str(request.form["voteUp"])).first()
            if count.rating is None: 
                count.rating = 0
            else:
                count.rating += 1
            
        flag_modified(count, "rating")
        db.session.merge(count)
        db.session.flush()
        db.session.commit()
        return redirect(f'/Myco-NET/{mycNet}/{itemType}')

@app.route('/', methods=['GET'])
@app.route('/Myco-NET')
@app.route('/Myco-NET/')
@app.route('/Mushroom')
@app.route('/Mushroom/')
@app.route('/Myco-NET/<mycNet>')
@app.route('/Myco-NET/<mycNet>/<itemType>')
def handle_redirect(mycNet = None, itemType = None):
    return redirect('/Mushroom/Grow-Guides')

@app.route('/Mushroom/')
@app.route('/Mushroom/<mycNet>')
@app.route('/Mushroom/<mycNet>/<itemType>')
def render_large_template(mycNet = None, itemType = None, items = None):
    pageToRender = 'myco-net-beta.html'
    if (mycNet == "GrowGuides" or mycNet == "Grow-Guides"):
        pageToRender = "mycoGrowingGuides.html"
        teks = getMycoNetBuilds()
        if itemType == None:
            items = teks
        else:
            # The replace on items is for more human readable name, might consider just renameing products
            items = {f"{itemType}": teks[itemType.replace('-', ' ')]}
    
    if (mycNet == "Identification"):
        pageToRender = "mycoIdentification.html"
        ids = getMycoNetIdentification()
        if itemType == None:
            items = ids
        else:
            # The replace on items is for more human readable name, might consider just renameing products
            items = {f"{itemType}": ids[itemType.replace('-', ' ')]}
    
    if (mycNet == "Equipment"):
        if itemType == None: itemType = keywords[0]
        print(type(model.Autocalves.query))
        
        baseQuery : BaseQuery = model.Autocalves.query
        items = baseQuery.filter(model.Autocalves.item_type == itemType).order_by(model.Autocalves.rating.desc()).all()
        # items = {}
        # for i in keywords:
        #     items[f'{i}'] = list([clave for clave in claves if clave.item_type == i])
        # pp.pprint(items)
        
    elif (mycNet == "Recipes"):
        items = model.Recipes.query.order_by(model.Recipes.rating.desc()).all()
        
    print(mycNet)
    return render_template(
            pageToRender, 
            items=items, 
            logo_txt=logo_txt,
            pages=getPages(),
            mycNet=mycNet, 
            keywords=keywords, 
            itemType=itemType,
            seo=getMeta()
        )

@app.route('/add/<code>/<quantity>', methods=['POST'])
def add_product_to_cart(code = None, quantity = None):
    print(code, quantity)
    return redirect(url_for('shop', page="shop"))

# Should add a thank you for ordering page, your order is being prepared when payment confirmed
YOUR_DOMAIN = 'https://bigfungus.ca'
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
        shipping_options=getShippingOptionsStripe(),
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
