# Reed College Food Reviewer

This repository provides a webservice that allows Reed College and public users to review the daily food options provided by the Bon Appétit Management Company at Reed Commons. The service relies on a scraper of Bon Appétit's website to populate a list of daily food items and allows users to vote up or down each item once.  The website is not currently hosted anywhere.

### server.py

`server.py` functions as the main handler of web server requests, populating the web page on GET requests and updating the database on PUT requests. Populating is handled by scraping utlities provided in `scraper.py` and `gen_html.py` which handles the front-end HTML code. Put requests simply set the updated database value so long as it is a valid entry.

### database.py

`database.py` defines the structure and functionality of the SQL database used to store entries provided by users such that each user may vote on a single menu item once. 

### scraper.py

`scraper.py` has two functions, a `scraper` that culls menu information from Bon [Appétit's website](https://reed.cafebonappetit.com/) for Reed College and a `timely_scraper` which only calls the `scraper` function at most every 10 minutes.

### gen_html.py and gen_item.py

`gen_html.py` simply populates an HTML script determining the front end appearence of the web page. `gen_item.py` populates a single item and the portion of the web page responsible for interacting with button. Together these two programs generate all the interactive features and appearence of the web site.
