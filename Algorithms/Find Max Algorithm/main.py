from find_max import find_max

# Example usage:
if __name__ == "__main__":
    data = []

    n = int(input("Enter number of elements: "))
    
    for _ in range(n):
        element = int(input("Enter element: "))
        data.append(element)

    print("Max value:", find_max(data))