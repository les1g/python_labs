# This program calculates the amount of caffeine remaining in the body after a given number of hours.
# The calculation is based on the half-life of caffeine, which is assumed to be 6 hours in this program.

# Step 1: User input for the initial caffeine amount in mg
caffeine_mg = float(input('Enter the caffeine in mg: '))

# Step 2: Set the half-life of caffeine (in hours)
half_life = 6  # Half-life of caffeine in hours

# Step 3: Calculate the remaining caffeine levels after 6, 12, and 24 hours
# The formula used is: remaining_caffeine = initial_caffeine * (0.5) ^ (time / half_life)

caffeine_level_hour6 = caffeine_mg * 0.5 ** (6 / half_life)  # Caffeine after 6 hours
caffeine_level_hour12 = caffeine_mg * 0.5 ** (12 / half_life)  # Caffeine after 12 hours
caffeine_level_hour24 = caffeine_mg * 0.5 ** (24 / half_life)  # Caffeine after 24 hours

# Step 4: Output the results, formatted to two decimal places
print(f'After 6 hours: {caffeine_level_hour6:.2f} mg')  # Display caffeine after 6 hours
print(f'After 12 hours: {caffeine_level_hour12:.2f} mg')  # Display caffeine after 12 hours
print(f'After 24 hours: {caffeine_level_hour24:.2f} mg')  # Display caffeine after 24 hours
