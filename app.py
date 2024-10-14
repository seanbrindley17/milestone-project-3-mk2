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


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


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
                flash(f"Welcome back, {session['user']}")
                return redirect(url_for("get_entries"))
            
            
            flash("Incorrect username or password")
            return redirect(url_for("login"))
            
        
        flash("Incorrect username or password")
        return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_new_entry", methods=["GET", "POST"])
def add_new_entry():
    if request.method == "POST":
        if "user" in session:
            entry = {
                "stroke": request.form.get("stroke_name"),
                "distance": request.form.get("distance"),
                "time": request.form.get("swim_time"),
                "date": request.form.get("swim_date"),
                "created_by": session["user"]
            }
            mongo.db.entries.insert_one(entry)
            flash("Time Added")
            return redirect(url_for("get_entries"))
        else:
            flash("Log in to add an entry")
            return redirect(url_for("login"))
    
    strokes = mongo.db.strokes.find()
    distances = mongo.db.distances.find()
    return render_template("new_entry.html", strokes=strokes, distances=distances)


@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    if request.method == "POST":
        edited_entry = {
            "stroke": request.form.get("stroke_name"),
            "distance": request.form.get("distance"),
            "time": request.form.get("swim_time"),
            "date": request.form.get("swim_date"),
        }
        mongo.db.entries.replace_one({"_id": ObjectId(entry_id)}, edited_entry)
        flash("Entry Edited")
        return redirect(url_for("get_entries"))
    
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    strokes = mongo.db.strokes.find()
    distances = mongo.db.distances.find()
    return render_template("edit_entry.html", entry=entry, strokes=strokes, distances=distances)


@app.route("/delete_entry/<entry_id>")
def delete_entry(entry_id):
    mongo.db.entries.delete_one({"_id": ObjectId(entry_id)})
    flash("Deleted")
    return redirect(url_for("get_entries"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
