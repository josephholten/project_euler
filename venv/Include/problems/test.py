class Immutable:
    def __setattr__(self, key, value):
        raise AttributeError(f"{self.__class__} has no attribute {key}")
        return None

    t = [None for i in range(3)]
    def __init__(self, a,b,c):
        self.t[0]=a; self.t[1]=b; self.t[2]=c

class Mutable:
    t = [None for i in range(3)]
    def __init__(self, args):
        self.t = args

    def __getitem__(self, item):
        return self.t[item]
    def __setitem__(self, key, value):
        self.t[key] = value
        return value

if __name__=="__mai__":
    x = Immutable(1,2,3)
    print(f"x: {x.t}")
    d = {x : 1}
    print(f"d[x]: {d[x]}")
    l = [1,2,5,7]
    y = Mutable(l)
    print(f"y[1]: {y[1]}")
    d2 = {y : 1}
    print(f"y: {y.t}, d2[y]: {d2[y]}")
    y[3] = 4                 # y wird geändert
    print(f"y: {y.t}, d2[y]: {d2[y]}")

def f(*x):
    if(len(x))==0:
        return "hallo"
    if(len(x))==1:
        return x[0]
    if(len(x))==2:
        return x[0]+x[1]
print(f())
print(f(1))
print(f(1,2))

