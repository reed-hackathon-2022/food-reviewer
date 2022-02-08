from flask import Flask, request
from scraper import timely_scrape
from vote_database import SQLiteVoteDatabase
from gen_html import gen_html
import os

# create Flask app
app = Flask(__name__)

# intialize database
database = SQLiteVoteDatabase('votes.db')

# route GET and PUT to handle_request()
@app.route("/", methods = ['GET', 'PUT'])
def handle_request():
    user = request.headers.get('X-Forwarded-For') # pythonanywhere specific
    # on GET populate the web page
    if request.method == 'GET':
        menu = timely_scrape()
        return gen_html(database, menu, user)
    # on PUT update database
    if request.method == 'PUT':
        json = request.get_json()
        item = json['item']
        value = int(json['value'])
        if value not in [-1, 0, 1]:
            return ""   
        database.set(user, item, value)
        return ""

# start test mode server
if __name__ == '__main__':
    app.run()
