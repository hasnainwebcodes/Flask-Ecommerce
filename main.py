from flask import Flask,render_template,request, session,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os,stripe
from flask_jwt_extended.exceptions import NoAuthorizationError, RevokedTokenError, FreshTokenRequired
import time
from math import floor
from werkzeug.utils import secure_filename as sf
from flask_mail import Mail
import json
from flask_jwt_extended import get_jwt, JWTManager,unset_jwt_cookies, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta




with open("config.json","r") as c:
    params= json.load(c)["params"]



    
app= Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-super-secret-key-change-this-in-production'
bcrypt= Bcrypt(app)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
blacklist = set()
stripe.api_key = ""
PUBLISHABLE_KEY ="pk_test_51SBVr9DRIV9EVyvDsJq69RKUGnOqwYd5bydXmwCkwwl1EaEEUMXX4TgfYiLX4OYZqmHsjPEpssI2yKYhQL75H7hP00QwBZuRF3"

app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False  # True only in production (HTTPS)
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
jwt = JWTManager(app)
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
    username= db.Column(db.String(30), nullable= False)
    amount= db.Column(db.Integer)
    status= db.Column(db.String(12), nullable= True)
    items= db.Column(db.Text, nullable= True)
    itemsize= db.Column(db.String(1), nullable= True)
    cod= db.Column(db.String(5), nullable= True)
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



    
@app.errorhandler(NoAuthorizationError)
def handle_missing_token(e):
    return redirect("/login")
@app.errorhandler(RevokedTokenError)
def handle_revoken_token(e):
    return redirect("/login")
@app.errorhandler(FreshTokenRequired)
def handle_fresh_token(e):
    return redirect("/login")
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist
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
@jwt_required(locations=["cookies"])
def add():
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
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
@jwt_required(locations=["cookies"]) 
def get(id):
     product= Products.query.filter_by(id=id).first()
     return render_template("shop-single.html", product= product)
@app.route("/products/<int:id>/edit", methods=["GET","POST"])
@jwt_required(locations=["cookies"])
def edit_product(id):
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
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
@jwt_required(locations=["cookies"])
def delete_product(id):
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
     product= Products.query.filter_by(id=id).first()
     db.session.delete(product)
     db.session.commit()
     return redirect("/products")
@app.route("/admin")
@jwt_required(locations=["cookies"])
def admin():
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
     users= Users.query.all()
     orders= Orders.query.all()
     products= Products.query.all()
     return render_template("admin.html", users=users, products= products, orders= orders)
@app.route("/uploader", methods=["POST"])
@jwt_required(locations=["cookies"])
def uploader():
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
     f=request.files['file1']
     f.save(os.path.join(app.config['File_name'],sf(f.filename)))
     time.sleep(5)
     return redirect("/admin")
@app.route("/place-order", methods=['POST'])
@jwt_required(locations=["cookies"])
def place_order():
     size= request.form.get('product-size')
     quantity= request.form.get('product-quanity')
     name= request.form.get('product-title')
     amount= int(quantity)*int(request.form.get('product-price'))
     return render_template("place_order.html", size=size, quantity=quantity, name=name, amount=amount)
@app.route("/orders/add", methods=['POST'])
@jwt_required(locations=["cookies"])
def add_order():
     username= request.form.get('user')
     amount= request.form.get('price')
     status= request.form.get('status')
     items= request.form.get('name')
     itemsize= request.form.get('size')
     quantity= request.form.get('quantity')
     adress= request.form.get('adress')
     cod= request.form.get('cod')
     if cod:
          order= Orders(cod="True",username=username, amount=amount,status=status,items=items,quantity=quantity, itemsize=itemsize, adress=adress)
          db.session.add(order)
          db.session.commit()
          try:
               mail.send_message("A new Order placed on site   "+ username, sender=params['gmail_user'],
                        recipients=[params['gmail_user']],
                        body="\n Product:"+items+"\n Quantity:"+quantity+"\n Size:"+itemsize+"\n Adress:"+adress+"\n cod:True \n Please Start shipping so that User doesn't face any inconvience")
          except Exception as e:
               print(e)
          return redirect("/products")
     else:
          order= Orders(cod="False",username=username, amount=amount,status=status,items=items,quantity=quantity, itemsize=itemsize, adress=adress)
          db.session.add(order)
          db.session.commit()
          try:
               mail.send_message("A new Order placed on site   "+ username, sender=params['gmail_user'],
                        recipients=[params['gmail_user']],
                        body="\n Product:"+items+"\n Quantity:"+quantity+"\n Size:"+itemsize+"\n Adress:"+adress+"\n cod:False \n Please Start shipping so that User doesn't face any inconvience")
          except Exception as e:
               print(e)
          return redirect("/payments/"+str(order.id))
@app.route("/payments/<int:id>", methods=['GET','POST'])
@jwt_required(locations=["cookies"])
def payments(id):
     if request.method== 'POST':
           try:
                  data=request.get_json()
                  amount= int(data.get("amount",500))
                  intent = stripe.Payment.create(
                      amount=amount,
                      currency="usd",
                      automatic_payment_methods={"enabled": True},
                  )
                  return jsonify({"clientSecret": intent.client_secret})
           except Exception as e:
                  return jsonify({"error": str(e)}),400   
     order= Orders.query.filter_by(id=id).first()
     return render_template("payments.html",order=order,publishable_key= PUBLISHABLE_KEY)
@app.route("/orders/<int:id>/edit", methods=['GET','POST'])
@jwt_required(locations=["cookies"])
def edit_order(id):
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
     order= Orders.query.filter_by(id=id).first()
     if request.method== 'POST':
          order.username= request.form.get('user')
          order.amount= request.form.get('price')
          order.status= request.form.get('status')
          order.items= request.form.get('name')
          order.itemsize= request.form.get('size')
          order.quantity= request.form.get('quantity')
          db.session.commit()
          return redirect("/admin")
     return render_template("edit_order.html", order=order)
@app.route("/orders/<int:id>/delete", methods=['POST'])
@jwt_required(locations=["cookies"])
def delete_order(id):
     data = json.loads(get_jwt_identity())
     if data['role'] != 'admin':
        return redirect("/login")
     order= Orders.query.filter_by(id=id).first()
     db.session.delete(order)
     db.session.commit()
     time.sleep(3)
     return redirect("/admin")
@app.route('/register', methods=['GET','POST'])
def register():
     if request.method== "GET":
          return render_template("register.html")
     data = request.get_json()
     if Users.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'Email already exists'}), 400

     hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
     new_user = Users(
        name=data['name'],
        email=data['email'],
        password=hashed_pw,
        phone=data.get('phone'),
        role= 'user'
    )
     db.session.add(new_user)
     db.session.commit()
     return jsonify({'msg': 'User registered successfully'}), 201
from flask_jwt_extended import set_access_cookies

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        user = Users.query.filter_by(name=data['name']).first()

        if not user or not bcrypt.check_password_hash(user.password, data["password"]):
            return jsonify({'msg': 'Invalid username or password'}), 401

        token = create_access_token(identity=json.dumps({'id': user.id, 'role': user.role}))
        resp = jsonify({'msg': 'Login successful', 'role': user.role})
        set_access_cookies(resp, token)
        return resp
    return render_template("login.html")
@app.route('/logout', methods=['GET','POST'])
@jwt_required(locations=["cookies"])
def logout():
     if request.method=='GET':
          return render_template("logout.html")
     jti = get_jwt()['jti']
     blacklist.add(jti)
     time.sleep(2)
     return redirect("/")



     










with app.app_context():
    db.create_all()
app.run(port=3010)
