# The requirements for a given year to be a leap year are:
# 1) The year must be divisible by 4
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400; therefore, both 1700 and 1800 are not leap years
# Some example leap years are 1600, 1712, and 2016.
# Write a program that takes in a year and determines whether that year is a leap year.

is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True