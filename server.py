from flask import Flask, request
from scraper import timely_scrape
from vote_database import VoteDatabase
from gen_html import gen_html
import pickle

app = Flask(__name__)

database = VoteDatabase()

@app.route("/", methods = ['GET', 'PUT'])
def handle_request():
    user = request.remote_addr
    if request.method == 'GET':
        menu = timely_scrape()
        return gen_html(database, menu, user)
    if request.method == 'POST':
        item = request.form['item']
        value = request.form['value']
        database.set(user, item, value)
        return ""
