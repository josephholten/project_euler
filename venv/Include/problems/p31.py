"""coin sums: how many ways can 2 pounds be made from any number of coins?"""

import copy

place_value = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
N = len(place_value)
c = [2]+[0]*(N-1)

def next_permutation(s, sub_comb):
    for i in range(len(sub_comb)):
        candidate = copy.deepcopy(sub_comb)
        candidate[i] -= 1
        missing = 2 - (s + sum(map(lambda x: x[0]*x[1], zip(sub_comb, place_value[(-len(sub_comb)):]))))
        print(missing)
        #candidate[i+1]
    #return missing

print(next_permutation(1, [1]+[0]*(N-2)))