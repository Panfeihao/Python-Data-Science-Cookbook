import numpy as np
np.random.seed(10)
x = [np.random.randint(10, 25)*1.0 for i in range(10)]


def min_max(x):
    return [round((xx-min(x))/(1.0*(max(x)-min(x))), 2) for xx in x]

print x
print min_max(x)