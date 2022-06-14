from flask import Flask, redirect, request, send_from_directory
from flask import render_template
import datetime
from time import sleep
from flask import Response
import pprint
pp = pprint.PrettyPrinter(indent=2)

from content.products import getProducts
from content.techniques import getMycoNetBuilds
from content.indentification import getMycoNetIdentification
from content.seo import getMeta, getPages

app = Flask(__name__)

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
        return redirect('/Home')
    
@app.route('/Products')
def productPageRedirect():
        return redirect('/Mushroom/Products')

@app.route('/Mushroom/Products')
def productPage():
        pageToRender = 'products.html',
        return render_template(
            pageToRender, 
            logo_txt=logo_txt,
            pages=getPages(),
            seo=getMeta()
        )

@app.route('/', methods=['GET'])
@app.route('/Home')
@app.route('/About')
def splash():
    return render_template(
        'home.html',
        logo_txt=logo_txt,
        pages=getPages(),
        seo=getMeta()
    )

@app.route('/time/')
def time():
    def streamer():
        while True:
            yield str(datetime.datetime.now())
            sleep(1)
    return Response(streamer())

@app.route('/Grow-Guides')
@app.route('/Grow Guides')
@app.route('/Myco-NET')
@app.route('/Mushroom/')
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
    if (mycNet == 'GrowGuides' or mycNet == 'Grow-Guides'):
        pageToRender = 'mycoGrowingGuides.html'
        teks = getMycoNetBuilds()
        if itemType == None:
            items = teks
        else:
            items = {f'{itemType}': teks[itemType.replace('-', ' ')]}
    
    if (mycNet == 'Identification'):
        pageToRender = 'mycoIdentification.html'
        ids = getMycoNetIdentification()
        if itemType == None:
            items = ids
        else:
            items = {f'{itemType}': ids[itemType.replace('-', ' ')]}

    print(mycNet)
    return render_template(
            pageToRender, 
            items=items, 
            logo_txt=logo_txt,
            pages=getPages(),
            mycNet=mycNet, 
            # keywords=keywords, 
            itemType=itemType,
            seo=getMeta()
        )
    
@app.route('/Identification/')
def handle_redirect_identification():
    return redirect('/Mushroom/Identification')


if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem') #certificate and key files  // ssl_context=context
    app.run('127.0.0.1', port=8000, debug=True)
    # serve(app, host='0.0.0.0', port=5000, url_scheme='https')
