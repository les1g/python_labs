import math

def math_function():
    """------------------------------------------------------
    Given three floating-point numbers x, y, and z, output
    x to the power of z, x to the power of (y to the power
    of z), the absolute value of (x minus y), and the
    square root of (x to the power of z).

    Output each floating-point value with two digits after
    the decimal point, which can be achieved as follows:
    print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')
    """
    print(math_function.__doc__)
    x = float(input())
    y = float(input())
    z = float(input())

    power_xz = math.pow(x, z)
    power_xyz = math.pow(x, math.pow(y, z))
    absolute_value = math.fabs(x - y)
    square_root = math.sqrt(math.pow(x, z))

    print(f'{power_xz:.2f} {power_xyz:.2f} {absolute_value:.2f} {square_root:.2f}')
    print('------------------------------------------------------')