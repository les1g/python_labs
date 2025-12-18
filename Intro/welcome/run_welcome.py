def welcome():
    """ This program takes a first name as the input, and
    outputs a welcome message to that name.
    """
    print(welcome.__doc__)
    user_name = input('What is your name? ')
    print('Hello', user_name, 'and welcome to CS Online!')

if __name__ == '__main__':
    welcome()