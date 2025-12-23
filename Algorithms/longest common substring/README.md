# Longest Common Substring Using Dynamic Programming  
Dynamic programming is a technique where solutions to smaller subproblems are stored and reused to efficiently solve a larger problem. The **Longest Common Substring (LCS)** problem is a classic example where dynamic programming provides a major performance improvement.

## How the Dynamic Programming Approach Works

To find the longest common substring between two strings, we build a **matrix** (a list of lists in Python).  
Each cell `(i, j)` in the matrix represents:

> The length of the longest common substring **ending at**  
> `str1[i]` and `str2[j]`.

### Filling the Matrix

For each pair of characters:

- If `str1[i] != str2[j]`  
  → `matrix[i][j] = 0`  
  (because a substring cannot continue)

- If `str1[i] == str2[j]`  
  → `matrix[i][j] = matrix[i-1][j-1] + 1`  
  (extend the previous matching substring)

As we fill the matrix, we track:

- The **maximum length** found so far  
- The **ending index** of that substring in either string  

Once the matrix is complete, we can extract the substring using Python slicing:

```python
substring = str1[start_index : end_index + 1]
```

## Space Optimization

A full matrix requires `O(n × m)` space, but we can do better.

### Key Insight  
To compute the value at `(i, j)`, we only need:

- The **current row**  
- The **previous row**  
- The **up-left** value `(i-1, j-1)`

This means:

- Only **two rows** are needed at any time  
- And with careful overwriting, even **one row** is enough

### How the Single-Row Optimization Works

Imagine we are filling row `i`:

- Columns **before** the current column `j`  
  → already updated (current row values)

- Columns **after** column `j`  
  → still hold values from the previous row

So one list can act as both:

- The current row (left side)  
- The previous row (right side)

This reduces memory usage from `O(n × m)` to **O(min(n, m))**.

## Why This Matters

- Dynamic programming transforms a slow brute‑force solution into an efficient one.  
- The longest common substring problem becomes solvable in **O(n × m)** time with **O(m)** space.  
- The space‑optimized version is especially useful for large strings, where a full matrix would be too large to store.