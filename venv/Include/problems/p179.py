import math
import bin_saving as bin
import time

primes = bin.decode_as_list(r"../files/primes.bin", 0)

def prime_factors(n):
    divisors = 1
    for k in primes:
        if k > n:
            break
        max = 0
        for i in range(1, n):
            if n % k == 0:
                n = int(n/k) # ?
            else:
                divisors *= i
                break
    return divisors

tally = 0
for n in range(2, 10**7):
    if prime_factors(n) == prime_factors(n+1):
        tally += 1
print(tally)

