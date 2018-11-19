# import necessary libraries
from flask import Flask, render_template, redirect

from scrape_mars import scrape
from flask_pymongo import PyMongo
import scrape_mars
import sys

# create instance of Flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():



    # Run scraped functions
    outputs = scrape_mars.scrape()
    # Insert forecast into database
    mars_db = {
        "title": outputs["title"],
        "teaser": outputs["teaser"],
        "featured_image_url": outputs["featured_image_url"],
        "mars_weather":outputs["mars_weather"],
        "tables" : outputs["tables"],
        # "hemisphere_image_urls": outputs["hemisphere_image_urls"]
    }

    print("this is mars_db",mars_db,file=sys.stderr)

    mongo.db.collection.update({},mars_db,upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


@app.route("/")
def index():

    # Find data
    mars_db = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars_db = mars_db)

if __name__ == "__main__":
    app.run(debug=True)
