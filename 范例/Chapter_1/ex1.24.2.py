#
from itertools import chain, compress, combinations, count, izip, islice

# 1
a = [1, 2, 3]
b = ['a', 'b', 'c']
print list(chain(a, b))

# 2
a = [1, 2, 3]
b = [1, 0, 1]
print list(compress(a, b))

# 3
a = [1, 2, 3, 4]
print list(combinations(a, 2))

# 4
a = range(5)
print a
b = izip(count(1), a)
for element in b:
    print element

# 5
a = range(100)
b = islice(a, 0, 100, 2)
print list(b)