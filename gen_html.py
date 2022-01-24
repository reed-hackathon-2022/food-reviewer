from vote_database import VoteDatabase
from gen_item import gen_item
from datetime import date

def gen_html(database, menu, user):
    output = []
    output.append(f'''
        <head>
        <title>Reed Daily Specials {date.today()}</title>
        <style>
        #headerContainer {{
            height: 105px;
            position: relative;
            background: #870400;
            color: #fff;
        }}
        @media only screen and (min-width: 1280px) {{
            #headerContainer {{
                height: 130px;
            }}
        }}
        #header {{
            position: relative;
            height: 100%;
            max-width: 1280px;
            margin: 0 auto;
        }}
        #header.reedHeaderCollapse #reedNav {{
            background: none;
            position: absolute;
            top: 15px;
            left: 100%;
            border: none;
            margin: 0;
            margin-left: -42px;
            height: 0;
            width: 27px;
            overflow: hidden;
            padding: 20px 0 0 0;
        }}
        a {{
            color: #b12;
            text-decoration-thickness: 1px!important;
            text-underline-offset: .2em!important;
        }}
        </style>
        </head>
        <div id="headerContainer">
        <header aria-label="Reed header" id="header" class="reedHeaderCollapse">
        <div id="nameplate">
        <h1><a title="Rate Reed's Daily Specials">Reed College</a></h1>
        </div>
        </header>
        </div>
        ''')
    output.append('<body style="background-color:#fffadb;">')
    for category, subcategories in menu:
        output.append(f'<h1 style="font-family:verdana;">{category}</h1>')
        for subcategory, items in subcategories:
            output.append(f'<h2>{subcategory}</h2>')
            for item in items:
                output.append(gen_item(item[0], item[1], database.get_item(item[0])))
    output.append('</body>')
    return '\n'.join(output)
