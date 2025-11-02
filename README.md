# 🛍️ Flask E-Commerce Web App

A complete e-commerce platform built using Flask, SQLAlchemy, and Stripe (test mode).
Supports authentication via JWT (cookies), admin panel, product management, orders, and payments.

⚙️ Tech Stack

Backend: Flask, SQLAlchemy, Flask-JWT-Extended, Flask-Bcrypt, Flask-Mail

Database: SQLite / MySQL (based on config)

Payments: Stripe (Test Mode)

Auth: JWT with cookies

Frontend: HTML (Jinja Templates)

📁 Setup Instructions

Clone the repository and navigate to the project folder.

Install dependencies:

pip install flask flask_sqlalchemy flask_bcrypt flask_jwt_extended flask_mail stripe


Create config.json with the following structure:

{
  "params": {
    "local_server": true,
    "local_url": "sqlite:///database.db",
    "prod_url": "",
    "upload_location": "static/uploads",
    "gmail_user": "your_email@gmail.com",
    "gmail_password": "your_app_password"
  }
}


Run the app:

python app.py


Access it at:
http://localhost:3010

👥 User Roles

Admin: Can manage users, products, and orders.

User: Can browse, order, and make payments.

🔑 Authentication

JWT stored in cookies.

Login creates a token, logout blacklists it.

Admin-only routes are protected and checked via role.

🧩 Main Routes and Functions
Route	Method	Auth	Description
/	GET	None	Redirects to products list.
/products	GET	None	Shows all products with pagination.
/products/<category>	GET	None	Filters products by category.
/products/<int:id>	GET	✅	Shows single product details.
/products/add	GET/POST	✅ (Admin)	Add a new product.
/products/<int:id>/edit	GET/POST	✅ (Admin)	Edit product details.
/products/<int:id>/delete	POST	✅ (Admin)	Delete product.
/uploader	POST	✅ (Admin)	Upload images/files.
/contact	GET/POST	None	Submit contact message (sends email).
/about	GET	None	Static about page.
/admin	GET	✅ (Admin)	Admin dashboard (users, products, orders).
/register	POST	None	Create new user account.
/login	POST	None	Login user (sets JWT cookie).
/logout	POST	✅	Logout and revoke token.
/place-order	POST	✅	Start order placement.
/orders/add	POST	✅	Save new order (COD or online).
/orders/<int:id>/edit	GET/POST	✅ (Admin)	Edit existing order.
/orders/<int:id>/delete	POST	✅ (Admin)	Delete order.
/payments/<int:id>	GET/POST	✅	Stripe checkout (test payments).
💳 Payments (Stripe Test Mode)

sk_test_... and pk_test_... keys used.

Transactions are simulated for testing only.

Fake payment cards (e.g. 4242 4242 4242 4242) can be used.

📬 Email Notifications

Uses Flask-Mail with Gmail SMTP.

Sends mail to admin on new orders or contact form submissions.

🧠 Models Overview

Users → id, name, email, role, password, phone, address

Products → id, name, description, price, stock, brand, images, category, specification

Orders → id, username, amount, status, items, quantity, size, address, cod, created date

Contact → name, email, phone, message

🚀 Notes

Run in venv for cleaner dependency management.

Set JWT_COOKIE_SECURE=True in production (HTTPS).

Use real Stripe keys for production payments.