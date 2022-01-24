import urllib.request
import time
from bs4 import BeautifulSoup

LAST_RUN = 0
LAST_RETURN = None

def timely_scrape():
    if time.time() - LAST_RUN > 600:
        LAST_RUN = time.time()
        LAST_RETURN = scrape()
        return LAST_RETURN
    return LAST_RETURN

def scrape():
    with urllib.request.urlopen('https://reed.cafebonappetit.com/') as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    sections = soup.findAll('section', {'data-type': 'daypart'})
    output = []
    for section in sections:
        specials = section.find('div', {'data-loop-index': '1'})
        subsections = specials.findAll('div', {'class': 'station-title-inline-block'})
        title = section['data-jump-nav-title']
        content = []
        for subsection in subsections:
            subtitle = subsection.find('h3').string
            items = subsection.findAll('button', {'class': 'h4 site-panel__daypart-item-title'})
            itemlist = [i.contents[0].strip() for i in items]
            content.append( (subtitle, itemlist) )
        output.append( (title, content) )
    return output
