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
from content.contactform import feedbackForm

app = Flask(__name__)

# Theming
logo_txt = 'big_fungus.png'
css = '/css/style.css'
PRODIMGS = "/static/product_images/"
assert css

from wtforms import validators, EmailField, Form, SelectField, TextAreaField

class RegistrationForm(Form):
    userType = SelectField("Type", choices=['1','2'])

class SKUs(Form):
    def formatChoices(type, category):
        if category == "oyster":
            vars = ["Pink Oyster", "Elm Oyster", "Blue Oyster", "Black Oyster", "Pearl Oyster", "King Oyster", "Italian Oyster", "Golden Oyster"]
        elif category == "medicinal":
            vars = ["Turkey Tail", "Lion's Mane", "Reishi", "Cordyceps"]
        elif category == "other":
            vars = ["Enoki", "Shiitake", "Hen of the Woods", "Chestnut", "Shimeji (White)", "Shimeji (Black)" ]
        else: 
            vars = []
        return [(PRODIMGS+i.lower().replace(" ", "_").replace("'", "")+"_"+type+".png", i) for i in vars]
    
    medicinal_tissue = SelectField("Select", 
        choices= formatChoices("tissue", "medicinal"), name="medicinal_tissue")
    
    oyster_tissue = SelectField("Select", 
        choices=formatChoices("tissue", "oyster"))
    
    other_tissue = SelectField("Select", 
        choices=formatChoices("tissue", "other"))
    
    medicinal_block = SelectField("Select", 
        choices=formatChoices("block", "medicinal"))
    
    oyster_block  = SelectField("Select", 
        choices=formatChoices("block", "oyster"))
    
    other_block  = SelectField("Select", 
        choices=formatChoices("block", "other"))
    
    kinshi_block = SelectField("Select", 
        choices=[
            (PRODIMGS+"kinshi.png","Italian Oyster"),
            (PRODIMGS+"kinshi.png","Turkey Tail"),
        ])

class RequestAQuote(Form):
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    body = TextAreaField(u'Request', [validators.optional(), validators.length(max=200)])


@app.route('/Mushroom/')
@app.route('/Mushroom')
@app.route('/mushroom')
@app.route('/Myco-NET/<mycNet>')
@app.route('/Myco-NET/<mycNet>/<itemType>')
@app.route('/About')
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

@app.route('/Myco-NET/Equipment')
@app.route('/Mushroom/Recipes')
@app.route('/Grow-Guides')
@app.route('/Grow Guides')
@app.route('/Myco-NET')
@app.route('/Myco-NET/')
@app.route('/Guides')
def guidesRedirect():
    return redirect('/Mushroom/Growing/Guides')

@app.route('/Myco-NET/GrowGuides/<tek>')
@app.route("/Mushroom/Grow-Guides/<tek>")
@app.route("/Mushroom/Grow-Guides/<tek>")
def ubRedirect(tek):
    return redirect(f"/Mushroom/Growing/Guides/{tek}")

@app.route('/', methods=['GET', 'POST'])
@app.route('/Home', methods=['GET', 'POST'])
def Home():
    emailForm = RequestAQuote(request.form)
    if request.method == 'POST' and emailForm.validate():
        feedbackForm(emailForm.email.data, emailForm.body.data)
        redirect(url_for('Products'))
        
    return render_template(
        'home.html',
        logo_txt=logo_txt,
        pages=getPages(),
        seo=getMeta(),
        emailForm = emailForm,
    )

@app.route('/Products', methods=['GET', 'POST'])
def Products():
        form = SKUs(request.form)
        emailForm = RequestAQuote(request.form)
        
        if request.method == 'POST' and emailForm.validate():
            feedbackForm(emailForm.email.data, emailForm.body.data)
            return redirect(url_for('Home'))

        products = getProductsClean()
        
        pageToRender = 'products.html',
        return render_template(
            pageToRender, 
            logo_txt=logo_txt,
            products=products,
            pages=getPages(),
            seo=getMeta(),
            form=form,
            emailForm=emailForm,
        )

@app.route('/Mushroom/Growing/Guides', methods=['GET', 'POST'])
@app.route('/Mushroom/Growing/Guides/<item>', methods=['GET', 'POST'])
def Guides(item = None):
    emailForm = RequestAQuote(request.form)
    if request.method == 'POST' and emailForm.validate():
        feedbackForm(emailForm.email.data, emailForm.body.data)
        return redirect(url_for('Home'))
    
    if (item == None):
        items = getMycoNetBuilds()
    else:
        items = getMycoNetBuilds(item.replace('-', ' '))
        
    return render_template(
            'mycoGrowingGuides.html', 
            items=items, 
            logo_txt=logo_txt,
            pages=getPages(),
            seo=getMeta(),
            emailForm=emailForm,
        )
        
@app.route('/Mushroom/Identification', methods=['GET', 'POST'])
@app.route('/Mushroom/Identification/<item>', methods=['GET', 'POST'])
def Identification(item = None):
    emailForm = RequestAQuote(request.form)
    if request.method == 'POST' and emailForm.validate():
        feedbackForm(emailForm.email.data, emailForm.body.data)
        return redirect(url_for('Home'))
    
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
            seo=getMeta(),
            emailForm=emailForm,
        )

if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem') #certificate and key files  // ssl_context=context
    app.run('127.0.0.1', port=8000, debug=True)
    # serve(app, host='0.0.0.0', port=5000, url_scheme='https')
