from flask import Blueprint, render_template

app_blueprint = Blueprint('app_blueprint',__name__)
#Variables 
popular_products = [
    {'name':'Johan Godinho T-Shirt','size':'small','price':5,'img':'/images/images.jfif','discounted':True,'discounted_amount':5},
    {'name':'Johan Godinho T-Shirt','size':'medium','price':10,'img':'/images/images.jfif','discounted':True,'discounted_amount':2},
    {'name':'Johan Godinho T-Shirt','size':'large','price':15,'img':'/images/images.jfif','discounted':False}
]

@app_blueprint.route('/')
def index():
    return render_template("index.html",popular_products=popular_products)

@app_blueprint.route('/about')
def about():
    return render_template("about.html")

@app_blueprint.route('/contact')
def contact():
    return render_template("contact.html")