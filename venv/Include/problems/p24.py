import time

#lexicographic permutations

ref = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def leastGreater(permutation, elem):
    for i, p in enumerate(permutation[::-1]):  # dealing with reverse sorted lists so this works (should be sort)
        if p>elem:
            return p

def findDecending(permutation):     # returns index of decending secequence
    r = permutation[::-1]
    decending = True
    index = 0
    for pos, i in enumerate(r):
        if i > r[pos + 1]:
            decending = False
            index = len(permutation)-1 - pos
            break
    return index

def next(permutation):
    #print(permutation)
    index = findDecending(permutation)-1    # this is position of element right before decending sequence
    current = permutation[index:]           # this is decending sequence (plus the index element)
    l_ind = current.index(leastGreater(current, current[0]))    # this is least greater element of the index element
    current[0], current[l_ind] = current[l_ind], current[0]            # swapping index elemement and the next greater
    return permutation[:index] + current[:1] + sorted(current[1:])   # leaving part before index alone, adding to that the next greater than the index element and then the sorted rest

permutation = ref
N = 10**6
t = time.time()
for i in range(1, N):  # gets the millionth permutation (since counting from 0)
    permutation = next(permutation)
t = time.time() - t
print(permutation)
print(f"{t*10**3} ms")   # v1: 1.7s

