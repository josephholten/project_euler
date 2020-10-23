# distinct powers

from math import *

powers = [100**100, 100**99]    # in reverse order

def insert(element):
    global powers
    if element > powers[0]:
        powers = [element] + powers
        return
    for i in range(len(powers)-1):
        if element < powers[i] and element > powers[i+1]:
            powers = powers[:i+1] + [element] + powers[i+1:]
            return
    if element < powers[-1]:
        powers += [element]

for a in range(100, 1, -1):
    for b in range(100, 1, -1):
        insert(a**b)
print(len(powers))