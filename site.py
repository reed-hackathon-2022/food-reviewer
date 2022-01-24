from vote_database import VoteDatabase

def site_get(database, menu, userID):
    output = []
    output.append(f'''
        <form method="POST">
        <input type="submit" value="Enter">
        </form>
        ''')
    for l1 in menu:
        output.append(f'<h1>{l1[0]}</h1>')
        for l2 in l1[1]:
            output.append(f'<h2>{l2[0]}</h2>')
            for l3 in l2[1]:
                output.append(f'''
                    {database.get_item(l3[0])} {l3[0]} {l3[1]}
                    <button>up</button>
                    <button>down</button>
                    {l3[0]}{l3[1]}
                    </br>
                    ''')
    return '\n'.join(output)
