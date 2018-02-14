from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
import itertools

#
data = load_iris()
x = data['data']
y = data['target']
col_names = data['feature_names']

#
plt.close('all')
plt.figure(1)
subplot_start = 321
col_numbers = range(0, 4)
#
col_pairs = itertools.combinations(col_numbers, 2)  # Coherent
plt.subplots_adjust(wspace=0.5)

# for col_pair in col_pairs:
#     print col_pair
#     plt.subplots(subplot_start)
#     plt.scatter(x[:, col_pair[0]], x[:, col_pair[1]], c=y)
#     plt.xlabel(col_names[col_pair[0]])
#     plt.ylabel(col_names[col_pair[1]])
#     subplot_start += 1
plt.scatter(x[:, 2], x[:, 3], c=y)
plt.show()
