def append_to_array(arr, value):
    """
    Appends a value to the end of an array (Python list).
    This mirrors the behavior of dynamic arrays.
    """
    arr.append(value)
    return arr

# Example usage:
if __name__ == "__main__":
    my_array = [1, 2, 3]
    print("Original array:", my_array)
    updated_array = append_to_array(my_array, 4)
    print("Updated array:", updated_array)