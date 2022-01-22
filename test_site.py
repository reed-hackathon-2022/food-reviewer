from flask import Flask, request
from scraper import scrape
from time import time()
app = Flask(__name__)







@app.route("/")
lastRun=0
contents=""
def test_site():
    if lastRun-time>600:
        results = scrape()
        output = []
        output.append('<ul>')
        for l1 in results:
            output.append(f'<li>{l1[0]}</li>')
            output.append('<ul>')
            for l2 in l1[1]:
                output.append(f'<li>{l2[0]}</li>')
                output.append('<ul>')
                for l3 in l2[1]:
                    output.append(f'<li>{l3}</li>')
                output.append('</ul>')
            output.append('</ul>')
        output.append('</ul>')
        contents=''.join(output)
     return contents
    
