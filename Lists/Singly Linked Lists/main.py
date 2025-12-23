from operations_module import Node, LinkedList, list_append, list_prepend, list_remove, print_list

def main():
    '''
    Demonstrates basic operations on a singly-linked list:
    - Creating an empty list
    - Appending nodes to the end
    - Prepending a node to the start
    - Removing nodes by value
    '''
    print("\n=== Singly-Linked List Demo ===\n")

    # Create list
    llist = LinkedList()
    print("Initial list:")
    print_list(llist)

    # Append nodes
    print("\nAppending 99...")
    list_append(llist, Node(99))
    print_list(llist)

    print("\nAppending 44...")
    list_append(llist, Node(44))
    print_list(llist)

    # Prepend node
    print("\nPrepending 66...")
    list_prepend(llist, Node(66))
    print_list(llist)

    # Remove node
    print("\nRemoving 99...")
    list_remove(llist, 99)
    print_list(llist)

    # Remove tail
    print("\nRemoving 44...")
    list_remove(llist, 44)
    print_list(llist)

    # Remove last remaining node
    print("\nRemoving 66...")
    list_remove(llist, 66)
    print_list(llist)

    print("\n=== End of Demo ===\n")

if __name__ == "__main__":
    main()