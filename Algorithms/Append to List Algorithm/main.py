from append_array import append_to_array
from append_linked_list import LinkedList

# Example usage:
if __name__ == "__main__":
    print("\n=== APPEND OPERATION DEMONSTRATION ===")
    print("This module demonstrates how append works for:")
    print("- A linked list (pointer-based structure)")
    print("- A Python list (dynamic array)")
    print("\nYou will see how each structure behaves and when each is useful.\n")

    # ---------------------------------------------------------
    # Demonstrate linked list append
    # ---------------------------------------------------------
    print("===============================================")
    print("APPENDING TO A LINKED LIST")
    print("-----------------------------------------------")
    print("How it works:")
    print("- A linked list stores elements in nodes connected by pointers.")
    print("- Appending creates a new node and updates the tail pointer.")
    print("- No shifting or resizing occurs (O(1) time).")
    print("Why it's important:")
    print("- Efficient for frequent insertions at the end or middle.")
    print("- Useful when memory is fragmented or unpredictable.\n")

    linked_list = LinkedList()
    linked_list_values = [1, 2, 3]

    print("Original linked list values:", linked_list_values)
    print("Enter values to append to the linked list (separated by spaces):")

    values_to_append = list(map(int, input().split()))
    for value in values_to_append:
        linked_list.append(value)
        linked_list_values.append(value)

    print("Updated linked list:", linked_list_values)
    print("When to use a linked list:")
    print("- When you need fast insertions/deletions.")
    print("- When you don't need fast random access.\n")

    # ---------------------------------------------------------
    # Demonstrate array append
    # ---------------------------------------------------------
    print("===============================================")
    print("APPENDING TO A PYTHON LIST (DYNAMIC ARRAY)")
    print("-----------------------------------------------")
    print("How it works:")
    print("- A Python list stores elements in contiguous memory.")
    print("- Appending adds the item to the end.")
    print("- If the array is full, Python resizes it (costly but rare).")
    print("Why it's important:")
    print("- Very fast for most append operations (amortized O(1)).")
    print("- Ideal for random access and indexing.\n")

    my_array = [1, 2, 3]
    print("Original array:", my_array)
    print("Enter values to append to the array (separated by spaces):")

    values_to_append_array = list(map(int, input().split()))
    for value in values_to_append_array:
        append_to_array(my_array, value)

    print("Updated array:", my_array)
    print("When to use an array:")
    print("- When you need fast indexing (arr[i]).")
    print("- When insertions/deletions are rare or mostly at the end.\n")

    # ---------------------------------------------------------
    # Summary comparison
    # ---------------------------------------------------------
    print("===============================================")
    print("SUMMARY: LINKED LIST VS ARRAY APPEND")
    print("-----------------------------------------------")
    print("Linked List:")
    print("- Append is always O(1).")
    print("- Great for frequent insertions/deletions.")
    print("- No random access (must traverse nodes).")

    print("\nArray (Python list):")
    print("- Append is amortized O(1).")
    print("- Great for fast indexing and iteration.")
    print("- Insertions/deletions in the middle require shifting (O(n)).")

    print("\nChoose a linked list when:")
    print("- You care about insertion speed.")
    print("- You don't need fast indexing.")

    print("\nChoose an array when:")
    print("- You need fast random access.")
    print("- You mostly append at the end.")