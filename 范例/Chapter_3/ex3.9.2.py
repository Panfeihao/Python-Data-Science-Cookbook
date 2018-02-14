from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
x = data['data']
print x.shape[0]

no_records = 10
x_sample_index = np.random.choice(range(x.shape[0]), no_records)
print x[x_sample_index, :]
