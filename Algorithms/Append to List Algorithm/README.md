# Append To A Linked List and Array (Python List) Algorithm

## Goal of this module

Explain how to append a new element to:

- A **linked list**, where data is stored in nodes connected by pointers  
- A **Python list** (dynamic array), where data is stored in contiguous memory  

This module demonstrates:

- How linked lists store data  
- How append works without shifting or resizing  
- Why linked lists behave differently from arrays  
- How Python lists handle append operations  

---

## How Linked List Append Works

A linked list is made of nodes, each containing:

- A value  
- A pointer to the next node  

Appending involves:

1. Creating a new node  
2. Updating the current tail’s `next` pointer  
3. Updating the list’s `tail` reference  

This operation is **O(1)** because no shifting or resizing is required.

---

## How Array Append Works

A Python list behaves like a **dynamic array**.

Appending involves:

1. Checking if there is space in the underlying array  
2. If full, allocating a larger block of memory and copying elements  
3. Placing the new item at the end  

Although resizing is expensive, Python performs it infrequently, so `append()` is **amortized O(1)**.

---

## Why this matters

Understanding the difference between linked lists and arrays helps explain:

- Why linked lists avoid shifting costs  
- Why arrays offer fast random access  
- When to choose one structure over the other  
- How append operations differ in performance and behavior  