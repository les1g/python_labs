# Import the random module
import random

def number_guess(num):
    """chooses a random number between 1 and
    100 by calling random.randint() and then
    output if the guessed number is too low,
    too high, or correct."""
    # Get a random number between 1-100
    random_number = random.randint(1, 100)

    # Compare parameter num to the random number
    if num == random_number:
        print(f'{num} is correct!')
    elif num < random_number:
        print(f'{num} is too low. Random number was {random_number}.')
    else:
        print(f'{num} is too high. Random number was {random_number}.')


if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)