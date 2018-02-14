# 1
def cylinder_vol(r):
    pi = 3.1415926
    def get_vol(h):
        return pi * r**2 * h
    return get_vol

# 2
radius = 10
find_volume = cylinder_vol(radius)

# 3
height = 10
print "Volume of cylinder of radius %d and height %d = %.2f cubic " \
      "units" % (radius, height, find_volume(height))
height = 20
print "Volume of cylinder of radius %d and height %d = %.2f cubic " \
      "units" % (radius, height, find_volume(height))

