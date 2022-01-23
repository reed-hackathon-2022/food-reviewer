from flask import Flask, request
from scraper import scrape
import pickle

app = Flask(__name__)





n = 0

@app.route("/", methods = ['GET', 'POST'])
def test_site():
    if request.method == 'GET':
        return test_site_get(request)
    if request.method == 'POST':
        test_site_post(request)
        return test_site_get(request)

def test_site_post(request):
    global n
    n += 1

def test_site_get(request):
    results = scrape()
    output = []
    output.append(f'''
        <form method="POST">
        <input type="submit" value="Enter">
        </form>
        <p> n is: {n} </p>
        ''')
    for l1 in results:
        output.append(f'<h1>{l1[0]}</h1>')
        for l2 in l1[1]:
            output.append(f'<h2>{l2[0]}</h2>')
            for l3 in l2[1]:
                output.append(f'''
                    {l3}
                    <button>up</button>
                    <button>down</button>
                    </br>
                    ''')
                              
    return '\n'.join(output)
