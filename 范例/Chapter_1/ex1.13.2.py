from math import log


def square_input(x):
    return x*x


# 1
#
def apply_func(func_x, input_x):
    return map(func_x, input_x)

# 2
a = [2, 3, 4]
print apply_func(square_input, a)
print apply_func(log, a)