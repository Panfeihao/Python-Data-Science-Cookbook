import numpy as np
from sklearn.preprocessing import scale

np.random.seed(10)
x = [np.random.randint(10, 25)*1.0 for i in range(10)]

x_centered = scale(x, with_mean=True, with_std=False)
x_standard = scale(x, with_mean=True, with_std=True)

print x
print x_centered
print x_standard
print "Orginal x mean = %0.2f, Centered x mean = %0.2f, Std dev of standard x = %0.2f" % \
      (np.mean(x), np.mean(x_centered), np.std(x_standard))