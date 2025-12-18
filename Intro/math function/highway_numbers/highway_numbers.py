highway_number = int(input())

if 1 <= highway_number <= 999:  # Valid range for interstate highways
    if 1 <= highway_number <= 99:  # Primary highways
        direction = "north/south" if highway_number % 2 != 0 else "east/west"
        print(f'I-{highway_number} is primary, going {direction}.')
    else:  # Auxiliary highways
        right_two_digits = highway_number % 100
        if 1 <= right_two_digits <= 99:
            direction = "north/south" if right_two_digits % 2 != 0 else "east/west"
            print(f'I-{highway_number} is auxiliary, serving I-{right_two_digits}, going {direction}.')
        else:
            print(f'I-{highway_number} is not a valid interstate highway number.')
else:  # Invalid highway number
    print(f'{highway_number} is not a valid interstate highway number.')
