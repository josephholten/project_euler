import math
import time
import collections

def coprime(a, b):
    return math.gcd(a, b)

# illegal python:
mylist = range(100)
good, bad = [], []
for x in mylist:
    (good, bad)[x < 50].append(x)


# step one: generate all primitive pythagorean triples below (or equal) threshold N
N = 100  # 10000

t = time.time()
# m: odd ints < N, n: odd ints < m

# TODO: make lazy...
primitive_triples = [sorted((m * n, (m ** 2 - n ** 2) // 2, (m ** 2 + n ** 2) // 2))
                     for m in range(1, N, 2) for n in range(1, m, 2) if coprime(m, n)]

print(f"Took {(time.time() - t):.5e} s to calculate primitive tuples up to {N}")

# step two: sort by [1]-component

primitive_triples.sort(key=lambda x: x[1])

# step three: add up number of cuboids

total = 0
M = 1
too_large = collections.deque([])
while total < 10e6:
    pass

