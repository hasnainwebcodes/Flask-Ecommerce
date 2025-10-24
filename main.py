from flask import Flask,render_template,request, session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import time
from math import floor
from werkzeug.utils import secure_filename as sf
from flask_mail import Mail
import json




with open("config.json","r") as c:
    params= json.load(c)["params"]



    
app= Flask(__name__)
app.config['File_name']= params["upload_location"]
app.secret_key= "Hi-this-is-key"
app.config.update(
     MAIL_SERVER= 'smtp.gmail.com',
     MAIL_PORT ='465',
     MAIL_USE_SSL= True,
     MAIL_USERNAME = params['gmail_user'],
     MAIL_PASSWORD =params['gmail_password']
     )
mail = Mail(app)
condition= params['local_server']
if condition:
     app.config['SQLALCHEMY_DATABASE_URI'] =params['local_url']
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
     app.config['SQLALCHEMY_DATABASE_URI'] =params['prod_url']
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Users(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(30), nullable= False)
    email= db.Column(db.String(40), unique = True, nullable = False)
    role= db.Column(db.String(5), nullable= False)
    password= db.Column(db.String(80), nullable= False)
    phone= db.Column(db.String(12), nullable= True)
    since= db.Column(db.DateTime, default= datetime.utcnow)
    address= db.Column(db.Text())

class Products(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    name= db.Column(db.String(30), nullable= False)
    description= db.Column(db.Text(),  nullable = False)
    price= db.Column(db.Integer, nullable= False)
    stock= db.Column(db.Integer, nullable= True)
    brand= db.Column(db.String(20), nullable = False)
    image1= db.Column(db.String(20), nullable = False)
    image2= db.Column(db.String(20), nullable = False)
    image3= db.Column(db.String(20), nullable = False)
    image4= db.Column(db.String(20), nullable = False)
    image5= db.Column(db.String(20), nullable = False)
    image6= db.Column(db.String(20), nullable = False)
    image7= db.Column(db.String(20), nullable = False)
    category= db.Column(db.String(10), nullable = False)
    specification= db.Column(db.Text(), nullable= False)

class Orders(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    userid= db.Column(db.Integer, nullable= False)
    amount= db.Column(db.Integer,)
    status= db.Column(db.String(12), nullable= True)
    items= db.Column(db.Text, nullable= True)
    itemsize= db.Column(db.String(1), nullable= True)
    quantity= db.Column(db.Integer, nullable= True)
    madeat= db.Column(db.DateTime, default= datetime.utcnow)
    adress= db.Column(db.Text(), nullable= False)
class Contact(db.Model):
    no=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False,)
    email=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(12),nullable=False)
    message=db.Column(db.String(500),nullable=False)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)



    

@app.route("/")
def home():
    return redirect("/products")
@app.route("/products")
def products():
    page = request.args.get('page')
    if not page or not page.isnumeric():
        page = 1
    else:
        page = int(page)

    posts = Products.query.all()
    per_page = 15
    last = floor(len(posts) / per_page)
    if page==last:
         posts = posts[(page-1)*per_page :]
    else:
         posts = posts[(page-1)*per_page : (page-1)*per_page + per_page]

    if page == 1:
        prev = "#"
        nex = "/?page=" + str(page + 1)
    elif page == last:
        nex = "#"
        prev = "/?page=" + str(page - 1)
    else:
        prev = "/?page=" + str(page - 1)
        nex = "/?page=" + str(page + 1)

    return render_template("shop.html", posts=posts, prev=prev, nex=nex)
@app.route("/products/<string:category>")
def products_cat(category):
    page = request.args.get('page')
    if not page or not page.isnumeric():
        page = 1
    else:
        page = int(page)

    posts = Products.query.filter_by(category=category).all()
    per_page = 15
    last = floor(len(posts) / per_page)
    if page==last:
         posts = posts[(page-1)*per_page :]
    else:
         posts = posts[(page-1)*per_page : (page-1)*per_page + per_page]

    if page == 1:
        prev = "#"
        nex = "/?page=" + str(page + 1)
    elif page == last:
        nex = "#"
        prev = "/?page=" + str(page - 1)
    else:
        prev = "/?page=" + str(page - 1)
        nex = "/?page=" + str(page + 1)

    return render_template("shop.html", posts=posts, prev=prev, nex=nex)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=["GET","POST"])
def contact():
     if (request.method=='POST') :
        name= request.form.get('name')
        email= request.form.get('email')
        phone= request.form.get('phone')
        message= request.form.get('message')
        entry=Contact(name=name,phone=phone,message=message,email=email)
        db.session.add(entry)
        db.session.commit()
        mail.send_message(
              name+' messaged from site',
              sender=params['gmail_user'],
              recipients=[params['gmail_user']],
              body=message + "\nPhone: " + phone + "\nFrom: " + email)
        return render_template("contact.html")
     return render_template("contact.html")
@app.route("/products/add", methods= ["GET","POST"])
def add():
     if request.method == "POST":
          name= request.form.get('name')
          description= request.form.get('description')
          spec= request.form.get('specification')
          price= request.form.get('price')
          stock= request.form.get('stock')
          brand= request.form.get('brand')
          category= request.form.get('category')
          img1= request.form.get('img1')
          img2= request.form.get('img2')
          img3= request.form.get('img3')
          img4= request.form.get('img4')
          img5= request.form.get('img5')
          img6= request.form.get('img6')
          img7= request.form.get('img7')
          product = Products(name=name,description=description,specification=spec, price=price, stock=stock,brand=brand, category=category, image1= img1, image2= img2, image3= img3, image4= img4, image5= img5, image6= img6, image7= img7)          
          db.session.add(product)
          db.session.commit()
          return redirect("/")
     return render_template("add_product.html")
@app.route("/products/<int:id>")
def get(id):
     product= Products.query.filter_by(id=id).first()
     return render_template("shop-single.html", product= product)
@app.route("/products/<int:id>/edit", methods=["GET","POST"])
def edit_product(id):
     if request.method=="POST":
          product= Products.query.filter_by(id=id).first()
          product.name= request.form.get('name')
          product.description= request.form.get('description')
          product.specification= request.form.get('specification')
          product.price= request.form.get('price')
          product.stock= request.form.get('stock')
          product.brand= request.form.get('brand')
          product.category= request.form.get('category')
          product.img1= request.form.get('img1')
          product.img2= request.form.get('img2')
          product.img3= request.form.get('img3')
          product.img4= request.form.get('img4')
          product.img5= request.form.get('img5')
          product.img6= request.form.get('img6')
          product.img7= request.form.get('img7')
          db.session.commit()
          return redirect("/products/"+ id)
     product= Products.query.filter_by(id=id).first()
     return render_template("edit_product.html",product=product)
@app.route("/products/<int:id>/delete", methods=["GET","POST"])
def delete_product(id):
     product= Products.query.filter_by(id=id).first()
     db.session.delete(product)
     db.session.commit()
     return redirect("/products")
@app.route("/admin")
def admin():
     users= Users.query.all()
     orders= Orders.query.all()
     products= Products.query.all()
     return render_template("admin.html", users=users, products= products, orders= orders)
@app.route("/uploader", methods=["POST"])
def uploader():
     f=request.files['file1']
     f.save(os.path.join(app.config['File_name'],sf(f.filename)))
     time.sleep(5)
     return redirect("/admin")
@app.route("/place-order", methods=['POST'])
def place_order():
     quantity= request.form.get('product-size')
     size= request.form.get('product-quanity')
     return quantity+size






with app.app_context():
    db.create_all()
app.run(port=3010)
