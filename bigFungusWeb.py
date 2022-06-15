from flask import Flask, redirect, request, send_from_directory, url_for
from flask import render_template
import datetime
from time import sleep
from flask import Response
import pprint
pp = pprint.PrettyPrinter(indent=2)

from content.products import getProductsClean, getProducts
from content.techniques import getMycoNetBuilds
from content.indentification import getMycoNetIdentification
from content.seo import getMeta, getPages

app = Flask(__name__)

# Theming
logo_txt = 'big_fungus.png'
css = '/css/style.css'
assert css

from wtforms import Form, SelectField

class RegistrationForm(Form):
    userType = SelectField("Type", choices=['1','2'])
    
class SKUMedicinal(Form):
    sku = SelectField("Type", choices=["Lion's Mane","Turkey Tail", "Cordyceps"])

class SKUOyster(Form):
    sku = SelectField("Type", choices=["Elm Oyster","Blue Oyster", "Black Oyster", "Pearl Oyster", "King Oyster", "Italian Oyster", "Golden Oyster"])

class SKUSpecial(Form):
    sku = SelectField("Type", choices=["Tidal Wave","Eclipse", "True Albino Teacher", "Golden Teacher"])

class SKUOther(Form):
    sku = SelectField("Type", choices=["Shiitake", "Hen of the Woods", "Enoki", "Cheatnut", "Shimeji (White)", "Shimeji (Black)" ])

    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = [form.username.data, form.email.data,
                    form.password.data]
        # db_session.add(user)
        print(user)
        print('Thanks for registering')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

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
@app.route('/About')
@app.route('/Mushroom/')
@app.route('/Mushroom/<mycNet>')
@app.route('/Mushroom/<mycNet>/<itemType>')
def deprecatedUrls():
    return redirect('/Home')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
    
@app.route('/Identification/')
def handle_redirect_identification():
    return redirect('/Mushroom/Identification')
    
@app.route('/Guides')
def guidesRedirect():
        return redirect('/Mushroom/Growing/Guides')

@app.route('/', methods=['GET'])
@app.route('/Home')
def Home():
    return render_template(
        'home.html',
        logo_txt=logo_txt,
        pages=getPages(),
        seo=getMeta()
    )

@app.route('/Products', methods=['GET', 'POST'])
def Products():
        form = RegistrationForm(request.form)
        
        formMedicinalTissue = SKUMedicinal(request.form)
        formOysterTissue = SKUOyster(request.form)
        formOtherTissue = SKUOther(request.form)
        
        if request.method == 'POST' and form.validate():
            user = [form.userType.data]
            print(user)
            print('Thanks for your interest')
            return redirect(url_for('Products'))
        
        pageToRender = 'products.html',
        return render_template(
            pageToRender, 
            logo_txt=logo_txt,
            products=getProductsClean(request.form),
            pages=getPages(),
            seo=getMeta(),
            form=form,
            formMedicinalTissue=formMedicinalTissue,
            formOysterTissue=formOysterTissue,
            formOtherTissue=formOtherTissue,
        )

@app.route('/Mushroom/Growing/Guides')
@app.route('/Mushroom/Growing/Guides/<item>')
def Guides(item = None):
    if (item == None):
        items = getMycoNetBuilds()
    else:
        items = getMycoNetBuilds(item.replace('-', ' '))
        
    return render_template(
            'mycoGrowingGuides.html', 
            items=items, 
            logo_txt=logo_txt,
            pages=getPages(),
            seo=getMeta()
        )
        
@app.route('/Mushroom/Identification')
@app.route('/Mushroom/Identification/<item>')
def Identification(item = None):
    
    pageToRender = 'mycoIdentification.html'
    ids = getMycoNetIdentification()
    if item == None:
        items = ids
    else:
        items = {f'{item}': ids[item.replace('-', ' ')]}

    print(item)
    return render_template(
            pageToRender, 
            items=items, 
            logo_txt=logo_txt,
            pages=getPages(),
            seo=getMeta()
        )

if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem') #certificate and key files  // ssl_context=context
    app.run('127.0.0.1', port=8000, debug=True)
    # serve(app, host='0.0.0.0', port=5000, url_scheme='https')
