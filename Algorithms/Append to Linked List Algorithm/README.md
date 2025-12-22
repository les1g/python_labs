## Linked List Append Algorithm (Python)
📌 Goal of this module
Show how to append a new element to a linked list, where data is stored in nodes connected by pointers.
This module demonstrates:
- How linked lists store data
- How append works without shifting or resizing
- Why linked lists behave differently from arrays

🧩 How Linked List Append Works
Concept
A linked list is made of nodes, each containing:
- A value
- A pointer to the next node
Appending involves:
- Creating a new node
- Updating the current tail’s next pointer
- Updating the list’s tail reference
No shifting, no resizing — just pointer updates.

🐍 Python Implementation
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



✔️ Example
lst = LinkedList()
lst.append(4)
lst.append(11)
lst.append(55)
lst.append(99)

current = lst.head
while current:
    print(current.value, end=" ")
    current = current.next
# Output: 4 11 55 99



🧠 Why this matters
Linked lists are essential for understanding:
- Pointer‑based data structures
- O(1) append operations
- Avoiding array shifting costs
- Implementing stacks, queues, and other ADTs

📂 Files in this module
- linked_list.py
- README.md

---

If you want, I can also generate:

- A **comparison README** (arrays vs linked lists)  
- A **complexity table**  
- A **visual diagram** for each structure


