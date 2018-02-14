from sklearn.preprocessing import MinMaxScaler
import numpy as np

np.random.seed(10)
x = np.matrix([np.random.randint(10, 25)*1.0 for i in range(10)])
print x
x = x.T
print x
minmax = MinMaxScaler(feature_range=(0.0, 1.0))
x_t = minmax.fit_transform(x)
print x_t

x = [np.random.randint(10, 25)*1.0 for i in range(10)]


def min_max_range(x, range_values):
    return [round(((xx-min(x))/(1.0*(max(x)-min(x))))*(range_values[1]-range_values[0]) + range_values[0], 2) for
            xx in x]

print min_max_range(x, (100,200))
