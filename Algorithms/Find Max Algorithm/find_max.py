def find_max(input_array):
    """
    Returns the largest value in input_array.
    Assumes the array has at least one element.
    """

    # Initialize max with the first element
    max_value = input_array[0]

    # Iterate through the remaining elements
    for i in range(1, len(input_array)):
        if input_array[i] > max_value:
            max_value = input_array[i]

    return max_value
