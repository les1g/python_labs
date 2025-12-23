# **Singly‑Linked List**

The goal of this project is to demonstrate:

- How singly‑linked list nodes work  
- How head and tail pointers are updated  
- How prepend and append operations modify only a few pointers  
- How removal works in a singly‑linked list  
- How an empty list behaves  
- How a list data structure simplifies list management  

This project is designed for learning and visualization, not for production use.

# **1. Node Structure**

A singly‑linked list node stores:

- The element’s **data**
- A **next** pointer referencing the next node  
  (or `None` if it is the last node)

# **2. List Data Structure**

The list structure stores:

- `head` — first node  
- `tail` — last node  

A list data structure is **optional**, but it makes operations easier because all metadata is stored in one object instead of multiple variables.

# **3. Append Operation (ListAppend)**

Adds a node to the **end** of the list.

Rules:

- If the list is empty:  
  - `head = newNode`  
  - `tail = newNode`
- Otherwise:  
  - `tail.next = newNode`  
  - `tail = newNode`


# **4. Prepend Operation (ListPrepend)**

Adds a node to the **front** of the list.

Rules:

- If the list is empty:  
  - `head = newNode`  
  - `tail = newNode`
- Otherwise:  
  - `newNode.next = head`  
  - `head = newNode`

# **5. Remove Operation (ListRemove)**

Removes the first node whose data matches the given value.

Handles all cases:

- Removing the **head**  
- Removing a **middle** node  
- Removing the **tail**  
- Removing from an **empty** list  

# **6. Printing the List**

`print_list.py` walks through the list from head to tail and prints each node’s data.  
This helps visualize pointer changes after each operation.

# **7. main.py — Demonstration**

The main program:

- Creates a list  
- Appends nodes  
- Prepends nodes  
- Removes nodes  
- Prints the list after each operation  

# **Why This Project Matters**

This project reinforces the core ideas of singly‑linked lists:

- Nodes are connected by pointers  
- `None` represents the end of the list  
- Prepend and append update only a few pointers  
- A list data structure simplifies management  
- Linked lists grow dynamically and do not require contiguous memory  

These concepts form the foundation for later topics such as:

- InsertAfter  
- Doubly‑linked lists  
- Stacks and queues  
- Hash tables with chaining  
- Graph adjacency lists  