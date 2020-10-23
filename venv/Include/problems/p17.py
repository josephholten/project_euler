ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
        9: "ninety"}
short_scale = {1: "thousand", 2: "million", 3: "billion", 4: "trillion", 5: "quadrillion", 6: "sextillion",
               7: "septillion", 8: "octillion", 9: "nonillion"}

import math

def num_to_word(n, zero_included=True):
    if n == 0:
        return "zero" if zero_included else ""
    if n < 1000:
        return bool(n // 100)*(ones[n//100]+" hundred")+\
               (bool(n // 100) and bool(n % 100))*(" and " + (tens[n//10 % 10] + bool(n % 10)*("-" + ones[n % 10]))
                              if n % 100 >= 20 else ones[n%100])
    res = ""
    while n > 1000:
        res += num_to_word(int(n // 10**((math.log10(n) // 3) * 3))) + " " + short_scale[int(math.log10(n)//3)]
        print(res)
        n = n // 10**((math.log10(n) // 3) * 3)
    return res

#print(num_to_word(1321))
for n in range(1000):
    print(num_to_word(n))