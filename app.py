import os

from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_entries")
def get_entries():
    entries = list(mongo.db.entries.find())
    return render_template("entries.html", entries=entries)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})
            
        if existing_user:
            flash("Username already exists, please try another")
            return redirect(url_for("register"))
        
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        if password != confirm_password:
            flash("Passwords don't match")
            return redirect(url_for("register"))
        
        registered_user = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registered_user)
        
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("get_entries"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                print(session)
                flash(f"Welcome back, {session["user"]}")
                return redirect(url_for("get_entries"))
            
            
            flash("Incorrect username or password")
            return redirect(url_for("login"))
            
        
        flash("Incorrect username or password")
        return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    print(session)
    session.pop("user")
    print(session)
    return redirect(url_for("login"))


@app.route("/add_new_entry", methods=["GET", "POST"])
def add_new_entry():
    if request.method == "POST":
        entry = {
            "stroke": request.form.get("stroke_name"),
            "distance": request.form.get("distance"),
            "time": request.form.get("swim_time"),
            "date": request.form.get("swim_date"),
            "created_by_user": session["user"]
        }
        mongo.db.entries.insert_one(entry)
        flash("Time Added")
        return redirect(url_for("get_entries"))
    
    strokes = mongo.db.strokes.find()
    distances = mongo.db.distances.find()
    return render_template("new_entry.html", strokes=strokes, distances=distances)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
