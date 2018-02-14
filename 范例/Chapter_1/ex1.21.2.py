#
import numpy as np
from StringIO import StringIO

#
in_data = StringIO("30kg,inr2000,31.11,56.33,1\n52kg,inr8000.35, 12, 16.7,2")

#
strip_func_1 = lambda x: float(x.rstrip("kg"))
strip_func_2 = lambda x: float(x.lstrip("inr"))

#
convert_funcs = {0: strip_func_1, 1: strip_func_2}

#
data = np.genfromtxt(in_data, delimiter=",", converters=convert_funcs)

#
in_data = StringIO("10,20,30\n56,,90\n33,46,89")
mss_func = lambda x: float(x.rstrip() or -999)
data_2 = np.genfromtxt(in_data, delimiter=",", converters={1: mss_func})