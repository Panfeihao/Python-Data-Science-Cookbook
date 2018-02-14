import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline


#
x = np.asmatrix([[1, 2], [2, 4]])
poly = PolynomialFeatures(degree=2)
poly.fit(x)
x_poly = poly.transform(x)

print "Original x variable shape", x.shape
print x
print "Transformed x variables", x_poly.shape
print x_poly
#
x_poly = poly.fit_transform(x)
print x_poly


#
data = load_iris()
x = data['data']
y = data['target']

estimator = DecisionTreeClassifier()
estimator.fit(x, y)
predicted_y = estimator.predict(x)
predicted_y_prob = estimator.predict_proba(x)
# predicted_y_lprob = estimator.predict_log_proba(x)
print predicted_y_prob[1]
# print predicted_y_lprob[1]

poly = PolynomialFeatures(3)
tree_estimator = DecisionTreeClassifier()

steps = [('poly', poly), ('tree', tree_estimator)]
estimator = Pipeline(steps=steps)
estimator.fit(x, y)
p_y = estimator.predict(x)
print p_y

