# reciprocal primes
# find (for d<1000) the decimal with the longest recurring cycle

def find(list, element, start=1):
    for i in range(len(list)-1-start, -1, -1):            # starting at the end, skipping start-indices
        if list[i] == element:
            return i
    return -1

def isCycle(decimal):               # gives false negative if cycle not at the end
    k = find(decimal, decimal[-1])  # first occurence of last element
    cycle_len = len(decimal) - k - 1
    if cycle_len == -1 or cycle_len > len(decimal)//2:
        return (False,0)
    else:
        r = decimal.copy()
        r.reverse()
        for i in range(1, cycle_len):
            if not r[i] == r[i+cycle_len]:
                return (False, 0)
        return (True, cycle_len)

def longDivision(div):                # if not a cycle returns whole decimal expansion, else only cycle
    decimal = []
    remainders = []
    a = 1
    b = 0
    while a<div:
        a *= 10
        decimal.append(0)
    while True:
        if a == 0:
            break  # decimal expansion ends
        d = a // div        # new decimal place
        decimal.append(d)
        b = div * d
        a -= b
        a *= 10
        remainders.append(a)
        c = isCycle(remainders)
        if c[0]:
            decimal = decimal[len(decimal)-c[1]:]
            break      # decimal expansion is periodical
    return c[1],decimal

if __name__ == "__main__":
    longest = 0
    for d in range(2, 1000):
        l = longDivision(d)
        if longest <= l[0]:
            longest = longDivision(d)[0]
    print(longest)