from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars
import sys

app = Flask(__name__)


conn = "mongodb://localhost:27017/"
client = pymongo.MongoClient(conn)
db = client.mars
collection = db.scrape_mars


@app.route("/")
def index():
    mars = collection.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    collection.replace_one({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
