def salary_calculation():
    """------------------------------------------------------
    The following program calculates yearly and monthly salary given
    an hourly wage. The program assumes 40 work hours per week and 50
    work weeks per year. Insert the correct number in the code below
    to print a monthly salary. Then run the program. The monthly salary
    should be 3333.333...
    """
    print(salary_calculation.__doc__)
    hourly_wage = float(input('What is your hourly wage? '))

    print('Annual salary is: ')
    print(hourly_wage * 40 * 50)
    print()

    print('Monthly salary is: ')
    print(((hourly_wage * 40 * 50) / 12))
    print('------------------------------------------------------')