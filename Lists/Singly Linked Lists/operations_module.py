# Singly Linked List Operations Module
# This module provides basic operations for singly linked lists,
# including appending a new node to the end of the list.

class Node: # Node class for singly linked list
    # Initialize a new node with given data
    def __init__(self, data):
        self.data = data
        self.next = None  # null pointer equivalent

class LinkedList: # Singly linked list class
    # Initialize an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

def list_append(llist, new_node): # Appends a new node to the end of the singly linked list
    # Empty list
    if llist.head is None:
        llist.head = new_node
        llist.tail = new_node
        return

    # Non-empty list
    llist.tail.next = new_node
    llist.tail = new_node

def list_prepend(llist, new_node): # Prepends a new node to the start of the singly linked list
    # Empty list
    if llist.head is None:
        llist.head = new_node
        llist.tail = new_node
        return

    # Non-empty list
    new_node.next = llist.head
    llist.head = new_node

def list_remove(llist, value): # Removes the first node with the specified value from the singly linked list
    if llist.head is None:
        return  # empty list

    # Removing head
    if llist.head.data == value:
        llist.head = llist.head.next
        if llist.head is None:
            llist.tail = None
        return

    # Removing non-head
    prev = llist.head
    curr = llist.head.next

    while curr is not None: # Traverse the list to find the node to remove
        if curr.data == value:
            prev.next = curr.next
            if curr == llist.tail:
                llist.tail = prev
            return
        prev = curr
        curr = curr.next

def print_list(llist): # Prints the elements of the singly linked list
    items = []
    curr = llist.head
    while curr is not None:
        items.append(str(curr.data))
        curr = curr.next
    print(" → ".join(items) if items else "(empty list)")

def find_next_node(llist, value):
    current_node = llist.head
    while current_node is not None:
        if current_node.data == value:
            return current_node
        current_node = current_node.next
    return None

def remove_node_after(llist, current_node):

    # Case 1: Remove head node if curNode is None
    if current_node is None:
        if llist.head is None:
            return  # empty list

        sucNode = llist.head.next
        llist.head = sucNode

        if sucNode is None:  # list became empty
            llist.tail = None
        return

    # Case 2: Remove node after curNode
    if current_node.next is not None:
        node_to_remove = current_node.next
        sucNode = node_to_remove.next
        current_node.next = sucNode

        if sucNode is None:  # removed tail
            llist.tail = current_node

    
