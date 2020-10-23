# number spiral diagonals

def nsd(side):
    corner_value = 1
    add = 0
    sum = 1
    for i in range(side//2):
        add += 2
        for i in range(4):
            corner_value += add
            sum += corner_value
    return sum

print(nsd(1001))