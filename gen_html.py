from vote_database import VoteDatabase
from datetime import date

def gen_html(database, menu, user):
    output = []
    output.append(f'''
        <head>
        <title>Reed Daily Specials {date.today()}</title>
        <style>
        .top {{
          background-color: #870400;
          padding-top: 1px;
          padding-left: 20px;
          padding-right: 0x;
          padding-bottom: 1px;
        }}
        .center {{
          padding-top: 5%;
          padding-left: 20px;
          padding-right: 0x;
          padding-bottom: 5%;
        }}
        </style>
        </head>
        <div class="top">
        <h1 style="color:#ffffff;font-size:500%;"> Rate Reed's Daily Specials </h1>
        </div>
        ''')
    output.append('<body style="background-color:#fffadb;">')
    for category, subcategories in menu:
        output.append(f'<h1 style="font-family:verdana;">{category}</h1>')
        for subcategory, items in subcategories:
            output.append(f'<h2>{subcategory}</h2>')
            for item in items:
                output.append(f'''
                    {database.get_item(item[0])} {item[0]} {' '.join(item[1])}
                    <button>up</button>
                    <button>down</button>
                    </br>
                    ''')
    output.append('</body>')
    return '\n'.join(output)
