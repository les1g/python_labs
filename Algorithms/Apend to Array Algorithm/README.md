# Array Append Algorithm (Python)

## 📌 Goal of this module
Demonstrate how appending an item to an **array-based structure** works.  
In Python, lists behave like **dynamic arrays**, meaning they automatically resize when needed.

This module shows:
- How array append works conceptually
- How Python implements append efficiently
- Why arrays differ from linked lists in how they handle insertions

---

## 🧩 How Array Append Works

### Concept
Arrays store elements in **contiguous memory**.  
Appending involves:

1. Checking if there is space at the end  
2. If not, allocating a larger block of memory  
3. Copying existing elements  
4. Adding the new item at the end  

Python hides these details, but the underlying behavior is the same.

---

## 🐍 Python Implementation

```python
def append_to_array(arr, value):
    """
    Appends a value to the end of an array (Python list).
    This mirrors the behavior of dynamic arrays.
    """
    arr.append(value)
    return arr