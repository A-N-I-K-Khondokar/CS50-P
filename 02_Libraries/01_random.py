# This one is a libraries in Python

import random
store=random.choice(["Heads","Tails"])
#print(store)


number=random.randint(1,10)
#print(number)


cards=['jack','queen','kings']
random.shuffle(cards)
for card in cards:
    print(card)



"""
keyword:
1. import
2. from
"""

''' from random import choice
 store=choice(["Heads","Tails"])
 print(store)  '''


