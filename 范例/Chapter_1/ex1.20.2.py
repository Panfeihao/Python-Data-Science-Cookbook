# 1
import numpy as np
from StringIO import StringIO
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")

# 2
data = np.genfromtxt(in_data, dtype=int, delimiter=",")

# 3
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",", usecols=(0,1))

# 4
in_data = StringIO("10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",", names="a,b,c")

# 5
in_data = StringIO("a,b,c\n10,20,30\n56,89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",", names=True)
