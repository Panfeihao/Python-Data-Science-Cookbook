a = {'a':1, 'b':2, 'c':3}
b = {x:pow(y,2) for x,y in a.items()}
print b

def process(x):
    if isinstance(x, str):
        return x.lower()
    elif isinstance(x, int):
        return x*x
    else:
        return -9

a = (1,2,-1,-2,'D',3,4,-3,'A')
b = tuple(process(x) for x in a)

print b