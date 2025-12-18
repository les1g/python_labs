def get_ordinal_suffix(number):
    if 11 <= number % 100 <= 13:  # Special case for 11th, 12th, 13th
        return 'th'
    last_digit = number % 10
    if last_digit == 1:
        return 'st'
    elif last_digit == 2:
        return 'nd'
    elif last_digit == 3:
        return 'rd'
    else:
        return 'th'

riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Find place in line.\n'
        '(6) Remove rider.\n'
        '(7) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '7':
    if user_input == '1':  # Add rider
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        name = input('Enter name:').strip().lower()
        print(name)
        line.insert(num_vips, name)
        num_vips += 1

    elif user_input == '3':  # Dispatch ride
        line = line[riders_per_ride:]
        if num_vips >= riders_per_ride:
            num_vips -= riders_per_ride
        if num_vips < riders_per_ride:
            num_vips -= num_vips

    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)

    elif user_input == '5':  # Find place in line
        find_rider = input('Enter name to find place in line: ').strip().lower()
        if find_rider in line:
            place_in_line = line.index(find_rider) + 1
            ordinal_suffix = get_ordinal_suffix(place_in_line)
            print(f'You are {place_in_line}{ordinal_suffix} in line.')
        else:
            print(f'{find_rider} is not in line.')

    elif user_input == '6':  # Remove rider
        remove_rider = input('Enter the name to remove from line: ').strip().lower()
        if remove_rider in line:
            line.remove(remove_rider)
            print(f'{remove_rider} has been removed from the line.')
        else:
            print(f'{remove_rider} is not in line.')

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)
