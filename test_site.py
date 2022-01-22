from flask import Flask, request
from scraper import scrape

app = Flask(__name__)







@app.route("/")
def test_site():
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
    return ''.join(output)
