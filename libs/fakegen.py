import random

def justify():
    candidate = [
            'changty', 'sky', 'roger', 'jimmy',
             'kfira', 'rachael', 'rinns', 'tclan' ]
    return candidate[random.randint(0, len(candidate)-1)]
