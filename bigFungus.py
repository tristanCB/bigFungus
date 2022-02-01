# save this as app.py
from operator import index
from re import template
from flask import Flask, redirect, request
from flask import render_template, url_for, session, stream_with_context
from flask import Response
from time import sleep
import datetime
# Local modules
# import content
from flask_sqlalchemy import SQLAlchemy
import os
import glob
# Payments https://stripe.com/docs/checkout/quickstart
import stripe

# This is your test secret API key.
stripe.api_key = os.environ["stripeApiKey"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://admin:{os.environ["pwd"]}@{os.environ["DBENDPOINT"]}/big-fungus-2'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Autocalves(db.Model):
    __tablename__ = 'kijiji_'                
    date_scrapped = db.Column(db.DateTime(), unique=False)
    price = db.Column(db.String(50), unique=False)
    img_href = db.Column(db.String(120), unique=False)
    img_alt = db.Column(db.String(120), unique=False)
    link = db.Column(db.String(250), primary_key=True)

    def __repr__(self):
        return f'<User {self.price!r}>'

class Logger(db.Model):
    __tablename__ = 'activity_'
    date_accessed = db.Column(db.DateTime(), unique=False)
    ip = db.Column(db.String(120), unique=False)
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)

    def __repr__(self):
        return f'Connecting IP > {self.ip!r}'

# DB interface
from content.products import getProducts, getShippingOptionsStripe


@app.teardown_request
def add_header(r):
    log = Logger(date_accessed=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ip=request.remote_addr)
    print(log)

    db.session.add(log)
    db.session.commit()
    return r

# # @app.after_request
# # def add_header(r):
# #     """
# #     Add headers to both force latest IE rendering engine or Chrome Frame,
# #     and also to cache the rendered page for 10 minutes.
# #     """
# #     print("adding header")
# #     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
# #     r.headers["Pragma"] = "no-cache"
# #     r.headers["Expires"] = "0"
# #     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# https://docs.gunicorn.org/en/stable/deploy.html
# 

pages = ["shop", "about", "clavereaper"]
distribution_ammounts = [1, 2, 3, 4, 5]
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
    
    return render_template(
        'index.html', 
        distribution_ammounts=distribution_ammounts, 
        products=getProducts(),
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

@app.route('/clavereaper')
def render_large_template():
    claves = Autocalves.query.all()
    print(claves)
    return Response(stream_template('claveFinder.html', rows=stream_with_context(claves), logo_txt=logo_txt,
        pages=pages,))

@app.route('/add/<code>/<quantity>', methods=['POST'])
def add_product_to_cart(code = None, quantity = None):
    print(code, quantity)
    return redirect(url_for('format', page="shop"))

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
