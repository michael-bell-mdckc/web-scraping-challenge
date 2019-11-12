from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/scrape_mars_app")


@app.route("/")
def index():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", mission_to_mars=destination_data)


@app.route("/scrape")
def scraper():
    marsData = scrape_mars.scrape_info()
    mongo.db.collection.update({}, marsData, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
