def array_append(array, new_item):
    # Get current size
    current_size = len(array)

    # Increase size by adding the new item at the end
    array.append(new_item)

    return array


# Example usage
arr = ["A", "B", "C"]
print("Before:", arr)
array_append(arr, "D")
print("After:", arr)