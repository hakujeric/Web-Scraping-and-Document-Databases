# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# client = pymongo.MongoClient()
# db = client.mars_db
# collection = db.mars_data


# Define the 'classDB' database in Mongo
# db = client.marsDB

# Define collections
# collection = db.Marsdata

@app.route("/")
def home():
    # mars_data = list(db.collection.find())[0]
    return  render_template('index.html', mars_data = mars_data)

@app.route("/scrape")
def web_scrape():
    mars_data = mongo.db.mars_data
    # db.collection.remove({})
    # Run the scrape function
    # costa_data = scrape_costa.scrape_info()
    mars_data = scrape_mars.scrape()
    # db.collection.insert_one(mars_data)
    # Update the Mongo database using update and upsert=True
    # mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)