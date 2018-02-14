#
import numpy as np
#
a_list = [1, 2, 3]
an_array = np.array(a_list)
#
an_array = np.array(a_list, dtype=float)

# Matrix
a_listoflist= [[1, 2, 3], [5, 6, 7], [8, 9, 10]]
a_matrix = np.matrix(a_listoflist, dtype=float)

#
#
def display_shape(a):
    print
    print a
    print
    print "Number of element in a = %d" % (a.size)
    print "Number of dimensions in a = %d" % (a.ndim)
    print "Rows and Columns in a", a.shape
    print

display_shape(a_matrix)

#
#
# 1.np.arange
created_array = np.arange(1, 10, dtype=float)
display_shape(created_array)

# 2.np.linspace
created_array = np.linspace(1, 10)
display_shape(created_array)

# 3.np.logspace
created_array = np.logspace(1, 10, base=10.0)
display_shape(created_array)

# 4.arange
created_array = np.arange(1, 10, 2, dtype=int)
display_shape(created_array)

# 5.E
ones_matrix = np.ones((3, 3))
display_shape(ones_matrix)

# 6.Zero Matrix
zeros_matrix = np.zeros((3, 3))
display_shape(zeros_matrix)

#
#
#
#
identity_matrix = np.eye(N=3, M=3, k=0)
display_shape(identity_matrix)
identity_matrix = np.eye(N=3, k=1)
display_shape(identity_matrix)

#
#
a_matrix = np.arange(9).reshape(3, 3)
display_shape(a_matrix)

#
#
a_matrix = np.arange(9).reshape(3, 3)
b_matrix = a_matrix.reshape(-1)
print a_matrix
print b_matrix
print "f_matrix ,row sum", a_matrix.sum(axis=1)

#
# T
print a_matrix
display_shape(a_matrix[::-1])

#
a_matrix = np.arange(9).reshape(3,3)
back_array = np.ravel(a_matrix)
display_shape(back_array)

a_matrix = np.arange(9).reshape(3,3)
back_array = a_matrix.flatten()
display_shape(back_array)

#
#
general_random_numbers = np.random.randint(1, 100, size=10)
print general_random_numbers
uniform_rnd_numbers = np.random.normal(loc=0.2, scale=0.2, size=(3, 3))
print uniform_rnd_numbers

# Grid
xx, yy, zz = np.mgrid[0:3, 0:3, 0:3]
xx = xx.flatten()
yy = yy.flatten()
zz = zz.flatten()
print xx
print yy
print zz