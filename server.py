from flask import Flask, request
from scraper import timely_scrape
from vote_database import VoteDatabase
from gen_html import gen_html
import pickle, asyncio

app = Flask(__name__)

with open('database', 'rb') as f:
    database = pickle.load(f)
tasks = []

async def save():
    with open('database', 'wb') as f:
        pickle.dump(database, f)

@app.route("/", methods = ['GET', 'PUT'])
def handle_request():
    user = request.remote_addr
    if request.method == 'GET':
        menu = timely_scrape()
        return gen_html(database, menu, user)
    if request.method == 'PUT':
        json = request.get_json()
        item = json['item']
        value = int(json['value'])
        if value not in [-1, 0, 1]:
            return ""   
        database.set(user, item, value)
        tasks.append(asyncio.create_task(save()))
        return ""

if __name__ = '__main__':
    app.run()
