def gen_item(name, diets, votes):
    return f'''
        {votes} {name} {' '.join(diets)}
        <button>up</button>
        <button>down</button>
        </br>
        '''
