import math

def note_frequency():
    """------------------------------------------------------
    On a piano, a key has a frequency, say f0. Each higher
    key (black or white) has a frequency of f0 * rn, where
    n is the distance (number of keys) from that key, and r
    is 2(1/12). Given an initial key frequency, output that
    frequency and the next 3 higher key frequencies.

    Output each floating-point value with two digits after
    the decimal point, then the units ("Hz"), then a newline,
    using the following statement:
    print(f'{your_value:.2f} Hz')
    """
    print(note_frequency.__doc__)
    f0 = float(input())
    n = 1.0
    r = math.pow(2.0, 1.0 / 12.0)
    # f0 * rn
    f1 = f0 * math.pow(r, n)
    n = 2
    f2 = f0 * math.pow(r, n)
    n = 3
    f3 = f0 * math.pow(r, n)

    print(f'{f0:.2f} Hz')
    print(f'{f1:.2f} Hz')
    print(f'{f2:.2f} Hz')
    print(f'{f3:.2f} Hz')
    print('------------------------------------------------------')