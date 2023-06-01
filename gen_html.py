from vote_database import SQLiteVoteDatabase
from gen_item import gen_item, script
from datetime import date

# add HTML string with front end specifications to the output
def gen_html(database, menu, user):
    output = []
    output.append(f'''
        <head>
        <title>Reed Daily Specials {date.today()}</title>
        <style>
        #headerContainer {{
            height: 70px;
            position: relative;
            background: #870400;
            color: #fff;
        }}
        #header {{
            position: relative;
            height: 100%;
            max-width: 1280px;
            margin: 0 auto;
        }}
        h1 {{
            font-family: verdana;
            font-size: 46px;
            font-weight: normal;
            line-height: normal;
            margin: 0.5em 0 0.25em;
        }}
        h2 {{
            font-family: verdana;
            font-size: 36px;
            font-weight: normal;
            line-height: normal;
            margin: 0.5em 25px 0.25em;
        }}
        h3 {{
            font-family: verdana;
            font-size: 26px;
            font-weight: normal;
            line-height: normal;
            margin: 0.5em 50px 0.5em;

        }}
        #center_body {{
            margin-left: 75px;
        }}
        </style>
        {script}
        </head>
        ''')
    # Add the header
    output.append('''<body style="background-color:#fffadb;margin:0px;">
        <div id="headerContainer">
        <header aria-label="Reed header" id="header">
        <h1 style="font-family:serif;font-size:56px;margin-top:0px;margin-left:20px;"><a>Rate Reed's Daily Specials</a></h1>
        </header>
        </div>
        <div id="center_body">
    ''')
    # populate the menu
    for category, subcategories in menu:
        output.append(f'<h1>{category}</h1>')
        for subcategory, items in subcategories:
            output.append(f'<h2>{subcategory}</h2>')
            for item in items:
                output.append('<h3>')
                output.append(gen_item(item[0], item[1], database.get_item(item[0]), database.get_single_vote(user, item[0])))
                output.append('</h3>')
    output.append('</div> </body>')
    return '\n'.join(output)
