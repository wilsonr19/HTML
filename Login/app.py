from flask import Flask,request,render_template,redirect,url_for,session
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
# import mysql.connector

app = Flask(__name__)
# app.secret_key = os.urandom(24)

# conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '1999', database = 'url')
# cursor = conn.cursor()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)

class user(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200), nullable = False)
	email = db.Column(db.String(200), nullable = False, unique = True)
	password = db.Column(db.String(200), nullable = False)


@app.route("/")
def base():
	return render_template("base.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/home")
def home():
	return render_template("home.html")
	# if 'id' in session:
	# 	return render_template("home.html")
	# else:
	# 	return redirect("/")



@app.route("/index")
def index():
	return render_template("index.html")

	
@app.route("/login_validation", methods =["POST"])
def login_validation():
	if request.method == "POST":
		email = request.form["email"]
		password = request.form["password"]
		check = user.query.filter_by(email = email).all()
		check = user.query.filter_by(password = password).all()
		if len(check) > 0:
			# session['id'] = user[0][0]
			return redirect("/home")
		else:
			return redirect("/login")
	else:
		return render_template("login.html")


@app.route("/register_validation", methods =["POST"])
def register_validation():
	if request.method == "POST":
		name = request.form["name"]
		email = request.form["email"]
		password = request.form["password"]
		user_add = user(name = name, email = email, password = password)
		db.session.add(user_add)
		db.session.commit()
		return redirect("/login")
	return render_template("register.html")
# @app.route("/login_validation", methods = ["GET", "POST"])
# def login_validation():
# 	email = request.form.get("email")
# 	password = request.form.get("password")

# 	cursor.execute("""SELECT * FROM 'sign' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}' """.format(email, password))
# 	users = cursor.fetchall()
# 	# return "The email is {} and The password is{}".format(email, password)
# 	if len(users)>0:
# 		return render_template("home.html")
# 	else:
# 		return render_template("login.html")

# 	return "Hello"

@app.route("/logout", methods =["GET"])
def logout():
	# session.pop('id')
	return redirect(url_for("/"))

if __name__ == "__main__":
	app.run(debug=True)