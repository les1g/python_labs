def longest_common_substring_optimized(str1, str2):
    # Create one row of the matrix.
    matrix_row = [0] * len(str2)

    # Variables to remember the largest value, and the row it
    # occurred at.
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        # Variable to hold the upper-left value from the
        # current matrix position.
        up_left = 0
        for col in range(len(str2)):
            # Save the current cell's value; this will be up_left
            # for the next iteration.
            saved_current = matrix_row[col]
        
            # Check if the characters match
            if str1[row] == str2[col]:
                matrix_row[col] = 1 + up_left
                
                # Update the saved maximum value and row,
                # if appropriate.
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0
                
            # Update the up_left variable
            up_left = saved_current

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1, 
    # up to and including max_value_row.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]