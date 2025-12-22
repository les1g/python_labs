class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """
        Appends a new node to the end of the linked list.
        Matches the pseudocode from the participation activity.
        """
        new_node = Node(value)

        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Case 2: List has elements
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1