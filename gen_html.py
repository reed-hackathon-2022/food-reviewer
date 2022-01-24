from vote_database import VoteDatabase

def gen_html(database, menu, user):
    output = []
    output.append(f'''
        <form method="POST">
        <input type="submit" value="Enter">
        </form>
        ''')
    for category, subcategories in menu:
        output.append(f'<h1>{category}</h1>')
        for subcategory, items in subcategories:
            output.append(f'<h2>{subcategory}</h2>')
            for item in items:
                output.append(f'''
                    {database.get_item(item[0])} {item[0]} {' '.join(item[1])}
                    <button>up</button>
                    <button>down</button>
                    </br>
                    ''')
    return '\n'.join(output)
