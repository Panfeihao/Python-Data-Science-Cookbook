# 1
a = range(1,10)
print a
b = ["a", "b", "c"]
print b

# 2
print a[0]

# 3
print a[-1]

# 4
print a[1:3]
print a[1:]
print a[-1:]
print a[:-1]

# 5
a = [1, 2]
b = [3, 4]
print a + b

# 6
print min(a), max(a)

# 7
if 1 in a:
    print "Element 1 is available in list a"
else:
    print "Element 1 is available in tuple a"

# 8
a = range(1,10)
print a
a.append(10)
print a
b = range(11,15)
a.extend(b)
print a

# 9
a_stack = []

a_stack.append(1)
a_stack.append(2)
a_stack.append(3)

print a_stack.pop()
print a_stack.pop()
print a_stack.pop()

# 10
a_queue = []

a_queue.append(1)
a_queue.append(2)
a_queue.append(3)

print a_queue.pop(0)
print a_queue.pop(0)
print a_queue.pop(0)

# 11
from random import shuffle
a = range(1,20)
print a
shuffle(a)
print a
a.reverse()
print a

a.sort()
print a

a.reverse()
print a