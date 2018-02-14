# 1
class SimpleIterable(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for x in range(self.start, self.end):
            yield x**2


# 2
c = SimpleIterable(1, 10)

# 3
tot = 0
for val in iter(c):
    tot += val
print tot

# 4
tot = 0
for val in iter(c):
    tot += val
print tot