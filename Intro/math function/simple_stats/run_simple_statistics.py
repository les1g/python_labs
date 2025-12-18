def simple_statistics():
    """------------------------------------------------------
    Given 4 floating-point numbers. Use a string
    formatting expression with conversion specifiers
    to output their product and their average as integers (rounded),
    then as floating-point numbers.
    """
    print(simple_statistics.__doc__)
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())

    product= num1 * num2 * num3 * num4
    average = (num1 + num2 + num3 + num4) / 4.0

    print(f"{product:.0f} {average:.0f}")
    print(f"{product:.3f} {average:.3f}")
    print('------------------------------------------------------')