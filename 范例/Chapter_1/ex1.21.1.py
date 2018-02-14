# 1
import numpy as np
from StringIO import StringIO
in_data = StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35, 12, 16.7,2")
data = np.genfromtxt(in_data, delimiter=",")