import random

def justify():
    candidate = [
             'sky', 'tclan', 'william', 'yiming',
             'rachael', 'michael', 'hugo', 'yugioh',
             'changty', 'rinns', 'jimmy', 'kfira' ]
    return candidate[random.randint(0, len(candidate)-1)]
