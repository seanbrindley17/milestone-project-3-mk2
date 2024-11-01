import os

from datetime import datetime
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


# Shows the user the entries created by them by matching the username to the session user cookie
@app.route("/get_entries", methods=["GET", "POST"])
def get_entries():
    if request.method == "POST":
        distance_filter = request.form.get("distance-filter")
        date_time_filter = request.form.get("date-time-filter")
        entries = list(mongo.db.entries.find({"created_by": session["user"]}))
        if distance_filter:
            entries = list(
                mongo.db.entries.find(
                    {"created_by": session["user"], "distance": distance_filter}
                )
            )
        if date_time_filter == "date-latest":
            entries = sorted(entries, key=lambda entry: entry["date"], reverse=True)
        elif date_time_filter == "date-earliest":
            entries = sorted(entries, key=lambda entry: entry["date"])
        elif date_time_filter == "time-fastest":
            entries = sorted(entries, key=lambda entry: entry[("time")])
        elif date_time_filter == "time-slowest":
            entries = sorted(entries, key=lambda entry: entry[("time")], reverse=True)
        return render_template("entries.html", entries=entries)
    entries = list(mongo.db.entries.find({"created_by": session["user"]}))
    return render_template("entries.html", entries=entries)


# Should be the default page a user sees if they aren't logged in
@app.route("/")
@app.route("/welcome")
def welcome():
    if session:
        return redirect(url_for("get_entries"))
    return render_template("welcome.html")


# Allows a user to register an account, storing details in the database.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
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
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(registered_user)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("get_entries"))
    return render_template("register.html")


# Allows a user to log in to the site and see their entries with their session user cookie
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                display_name = existing_user["first_name"]
                session["user"] = request.form.get("username").lower()
                flash(f"Welcome back, {display_name}")
                return redirect(url_for("get_entries"))
            flash("Incorrect username or password")
            return redirect(url_for("login"))
        flash("Incorrect username or password")
        return redirect(url_for("login"))
    return render_template("login.html")


# Logs the user out by popping the session user cookie out of storage.
# A pop up confirmation box contains the function call button.
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Allows the user to add an entry.
# Also stores their username to allow display of only entries created by that user
@app.route("/add_new_entry", methods=["GET", "POST"])
def add_new_entry():
    if request.method == "POST":
        if "user" in session:
            minutes = request.form.get("minutes")
            seconds = request.form.get("seconds")
            milliseconds = request.form.get("milliseconds")
            race_time = minutes + ":" + seconds + "." + milliseconds
            date_str = request.form.get["swim_date"]
            formatted_date = datetime.strptime(date_str, "%d %B, %Y")
            entry = {
                "stroke": request.form.get("stroke_name"),
                "distance": request.form.get("distance"),
                "time": race_time,
                "date": formatted_date,
                "created_by": session["user"],
            }
            mongo.db.entries.insert_one(entry)
            flash("Time Added")
            return redirect(url_for("get_entries"))
        flash("Log in to add an entry")
        return redirect(url_for("login"))
    strokes = mongo.db.strokes.find()
    distances = mongo.db.distances.find()
    return render_template("new_entry.html", strokes=strokes, distances=distances)


# Allows user to edit an entry.
@app.route("/edit_entry/<entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    if request.method == "POST":
        if "user" in session:
            minutes = request.form.get("minutes")
            seconds = request.form.get("seconds")
            milliseconds = request.form.get("milliseconds")
            race_time = minutes + ":" + seconds + "." + milliseconds
            date_str = request.form.get("swim_date")
            formatted_date = datetime.strptime(date_str, "%d %B, %Y")
            edited_entry = {
                "stroke": request.form.get("stroke_name"),
                "distance": request.form.get("distance"),
                "time": race_time,
                "date": formatted_date,
                "created_by": session["user"],
            }
            mongo.db.entries.replace_one({"_id": ObjectId(entry_id)}, edited_entry)
            flash("Entry Edited")
            return redirect(url_for("get_entries"))
    entry = mongo.db.entries.find_one({"_id": ObjectId(entry_id)})
    race_time_split = entry["time"].split(":")
    minutes = race_time_split[0]
    race_time_split_seconds = race_time_split[1].split(".")
    seconds = race_time_split_seconds[0]
    milliseconds = race_time_split_seconds[1]
    strokes = mongo.db.strokes.find()
    distances = mongo.db.distances.find()
    return render_template(
        "edit_entry.html",
        entry=entry,
        strokes=strokes,
        distances=distances,
        minutes=minutes,
        seconds=seconds,
        milliseconds=milliseconds,
    )


# Will delete an entry when called on it.
# There's a pop up confirmation before this happens.
@app.route("/delete_entry/<entry_id>")
def delete_entry(entry_id):
    mongo.db.entries.delete_one({"_id": ObjectId(entry_id)})
    flash("Deleted")
    return redirect(url_for("get_entries"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
