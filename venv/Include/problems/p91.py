import math

side_length = 50  # should be 50
# implied O=(0,0)

# triangle OPQ, named in counterclockwise order, starting at O

total_triangles = 0

# start off with all triangles with right angle at O
o = side_length ** 2  # for x_q and y_p there are each side_length number of options
total_triangles += o

# continue with P=(x,y) free (y<x)
# for each P=(x,0) there are side_length number of right triangles
p = side_length ** 2

for x in range(1, side_length + 1):
    for y in range(1, side_length + 1):  # only consider points below x=y-diagonal
        _x = x // math.gcd(x, y)
        _y = y // math.gcd(x, y)
        # P = (x,y)
        # (x-0)//y           == number of triangles upto x=0
        # (side_length-y)//x == number of triangles upto y=side_length
        print(x, y, min(x // _y, (side_length - y) // _x))
        p += min(x // _y, (side_length - y) // _x)

p *= 2  # because we can mirror all points along x=y - axis to give us points with right angle at Q
total_triangles += p
print(total_triangles)
