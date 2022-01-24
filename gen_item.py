def gen_item(name, diets, votes):
    up = '▲'
    down = '▼'
    return f'''
        {down} {votes} {up} {name} {' '.join(diets)}
        </br>
        '''
