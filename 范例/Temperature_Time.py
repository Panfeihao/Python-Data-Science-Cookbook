#
def TTC(s, d, v, p, T1, T2):
    r = p * 10**(-3)/(s*v*d)  # k/s
    t = (T2 - T1) / r  # s
    t = t/60  # min
    return r, t


#
shc_air = 1.0  # KJ/(Kg*k) Specific Heat Capacity of Air (0 C)
density = 1.29  # Kg/m^3 (0 C 1atm)
volume = 100  # m^3
power = 2400  # W J/s
T1 = 10  # C
T2 = 26  # C

#
R, T = TTC(shc_air, density, volume, power, T1, T2)
print R
print T
