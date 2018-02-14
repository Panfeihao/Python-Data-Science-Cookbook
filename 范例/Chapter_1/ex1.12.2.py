# 1
def sum_square(x):
    def square_input(x):
        return x*x
    return sum([square_input(x1) for x1 in x])

# 2
print sum_square([2, 4, 5])