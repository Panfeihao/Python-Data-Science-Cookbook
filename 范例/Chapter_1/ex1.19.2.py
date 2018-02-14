print zip(range(1, 5), range(1, 5))

# x, y = zip(*out)
# print x, y

a = (2, 3)
print pow(*a)

a_dict = {"x":10, "y":10, "z":10, "x1":10, "y1":10, "z1":10, }

def dist(x,y,z, x1,y1,z1):
    return abs((x-x1) + (y-y1) + (z-z1))

print dist(**a_dict)


#
def any_sum(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot
print any_sum(1, 2)
print any_sum(1, 2, 3)
