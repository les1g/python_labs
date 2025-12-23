from operations_module import *

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
    print("1. Creating an empty singly-linked list.")
    llist = LinkedList()
    print("Initial list:", end=" ")
    print_list(llist)


    # Append nodes
    print("\n2. Appending nodes to the list.")
    print("Appending 99...")
    list_append(llist, Node(99))
    print("Appending 23...")
    list_append(llist, Node(23))
    print("Appending 44...")
    list_append(llist, Node(44))
    print("List after appending:", end=" ")
    print_list(llist)

    # Prepend node
    print("\n3. Prepending nodes to the list.")
    print("Prepending 66...")
    list_prepend(llist, Node(66))
    print("Prepending 77...")
    list_prepend(llist, Node(77))
    print("List after prepending:", end=" ")
    print_list(llist)

    # Remove node
    print("\n4. Removing nodes from the list.")
    print("Removing 77...") 
    list_remove(llist, 77)
    print("List after removing (head):", end=" ")
    print_list(llist)
    print("Removing 99...")
    list_remove(llist, 99)
    print("List after removing:", end=" ")
    print_list(llist)
    print("Removing 44...")
    list_remove(llist, 44)
    print("List after removing (tail):", end=" ")
    print_list(llist)
    
    # Remove at specific value
    print("\n5. Removing nodes at specific values.")
    print("appending 10, 20, 30...")
    list_append(llist, Node(10))
    list_append(llist, Node(20))
    list_append(llist, Node(30))
    print("List before removals:", end=" ")
    print_list(llist)
    print("Removing the node after 10...")
    remove_node_after(llist, 10)
    print("List after removing the node after 10:", end=" ")
    print_list(llist)

    print("\n=== End of Demo ===\n")

if __name__ == "__main__":
    main()