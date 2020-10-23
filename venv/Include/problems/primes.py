import math
import bin_saving as bin
import time

bound = 10**7
numbers = list(range(bound+1))
primes = []
def write_primes(bound):
    with open(r"../files/primes_fix.bin", "wb") as primes_file:
        t1 = time.time()
        for n in numbers[2:int(math.sqrt(bound))]:
            if n == 0:
                continue
            for k in range(n,bound//n+1):
                numbers[n*k]=0
        t2 = time.time()
        print(f"finished in: {t2-t1}")
        for n in numbers[2:]:
            if n != 0:
                bin.write_word_fix(n, primes_file)

if __name__=="__main__":
    #write_primes(bound)
    primes = bin.decode_as_list(r"../files/primes_fix.bin", 10**7)
    for i,p in enumerate(primes):
       if p > primes[i+1]:
           print(f"Error at {i}")
    print(primes[6541:6541+20])
