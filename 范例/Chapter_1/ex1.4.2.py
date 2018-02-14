# 1
a_tuple = (1, 2, 'a')
b_tuple = 1, 2, 'c'

# 2
print b_tuple[0]
print b_tuple[-1]
# 3
try:
    b_tuple[0] = 20
except:
    print "Can't not change value of tuple by index"

# 4
#
c_tuple = (1, 2, [10, 20, 30])
c_tuple[2][0] = 100
print c_tuple

# 5
#
print a_tuple + b_tuple

# 6
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print a[1:]
print a[1:3]
print a[1:6:2]
print a[:-1]

# 7
print min(a), max(a)

# 8
if 1 in a:
    print "Element 1 is available in tuple a"
else:
    print "Element 1 is not available in tuple a"