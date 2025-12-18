# Task 1
# Complete the function to print the first X
# number of characters in the given string
def print_first(mystring, x):
    print(mystring[:x])

print('\nexpected output: WGU')
print_first(mystring='WGU College of IT', x=3)

# Task 2
# Complete the function to return the last X
# number of characters in the given string
def get_last(mystring, x):
    last_x = mystring[-x:]
    return last_x

print('\nexpected output: IT')
print(get_last('WGU College of IT', 2))

print('\nexpected output: College of IT')
print(get_last('WGU College of IT', 13))

# task 3
# Complete the function to return True
# if the word WGU exists in the given string
# otherwise return False
def contains_WGU(mystring):
    if 'WGU' in mystring:
        return True
    else:
        return False

print('\nexpected output: True')
print(contains_WGU('WGU College of IT'))

# task 4
# Complete the function to
# print all the words in the given string
def print_words(mystring):
    print(mystring.split())

print('\nexpected output: [\'WGU\', \'College\', \'of\', \'IT\']')
print_words('WGU College of IT')

# task 5
# Complete the function to combine the words
# into a sentence and return a string
def combine_words(words):
    space = ' '
    words_string = space.join(words)
    return words_string

print('\nexpected output: WGU College of IT')
print(combine_words(['WGU', 'College', 'of', 'IT']))

# task 6
# Complete the function to replace the word
# WGU with Western Governors University
# and print the new string
def replace_wgu(mystring):
    if 'WGU' in mystring:
        print(mystring.replace('WGU', 'Western Governors University'))

print('\nexpected output: Western Governors University Rocks')
replace_wgu('WGU Rocks')

# task 7
# Complete the function to remove the
# word WGU from the given string
# ONLY if it's not the first word and return the new string
def remove_wgu(mystring):
    if mystring[0:3] != 'WGU':
        if 'WGU' in mystring:
            new_str = mystring.replace('WGU', '')
        else:
            new_str = mystring
    else:
        new_str = mystring
    return new_str

print('\nexpected output: WGU Rocks')
print(remove_wgu('WGU Rocks'))

# task 8
# Complete the function to remove trailing spaces from the
# first string and leading spaces from the second string
# and return the combined strings
def remove_spaces(string1, string2):
    string1 = string1.rstrip()
    string2 = string2.lstrip()
    combined_strings = string1 + string2
    return combined_strings

print('\nexpected output: WGU Rocks-You know it!')
print(remove_spaces('WGU Rocks    ', '  -You know it!'))

# task 9
# Complete the function to print the
# specified hourly rate with two decimals
def display_hourly_rate(rate):
    print(f'${rate:.2f}')

print('\nexpected output: $34.79')
display_hourly_rate(34.789123)

# task 10
# Complete the function to return the
# number of uppercase letters in the given string
def count_upper(mystring):
    count = 0
    for letter in mystring:
        if letter.isupper() == True:
            count += 1

    return count

print('\nexpected output: 4')
print(count_upper('Welcome to WGU'))