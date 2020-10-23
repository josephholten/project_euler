# 1000-digit fibbonacci number

from math import *

bound = 10**999  # this is the first number to have 1000 digits

current = 1
last = 1

index = 2
while current <= bound:                     # very short fib calculator
    current, last = current+last, current
    index += 1
print(current)
print(index)
