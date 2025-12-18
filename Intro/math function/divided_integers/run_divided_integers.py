def divided_integers():
    """------------------------------------------------------
    a program that reads integers user_num and div_num as input,
    and outputs user_num divided by div_num three times using
    floor divisions.
    """
    print(divided_integers.__doc__)
    user_num = int(input('Enter the first number: '))
    div_num = int(input('Enter the number it will be divided into: '))

    result = user_num // div_num
    result2 = result // div_num
    result3 = result2 // div_num
    print(f'{user_num} divided by {div_num} is: {result}')
    print(f'{result} divided by {div_num} is: {result2} ')
    print(f'{result2} divided by {div_num} is: {result3}')
    print('------------------------------------------------------')