# **Fibonacci Numbers Using Recursion and Dynamic Programming**

Computing Fibonacci numbers is a classic example used to demonstrate the difference between **naive recursion** and **dynamic programming**.  
Both approaches produce the same result, but their performance differs dramatically.

# **How the Recursive Approach Works**

The recursive Fibonacci function directly follows the mathematical definition:

```
F(0) = 0
F(1) = 1
F(n) = F(n−1) + F(n−2)
```

The recursive implementation calls itself twice for each term:

```python
def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
```

### What Happens Internally

- Each call branches into **two more calls**  
- This creates a **binary recursion tree**  
- Many values are computed **over and over again**  
- Time complexity grows **exponentially**

For example, computing `F(10)` causes dozens of repeated calls to `F(5)`, `F(4)`, `F(3)`, etc.

This approach is simple but extremely inefficient for larger inputs.

# **How the Dynamic Programming Approach Works**

Dynamic programming avoids repeated work by **storing the results of subproblems**.

Instead of recomputing `F(n−1)` and `F(n−2)` many times, we compute each Fibonacci number **once** and reuse it.

### Iterative DP Implementation

```python
def dynamic_fibonacci(n):
    if n == 0:
        return 0

    previous = 0
    current = 1

    for _ in range(1, n):
        next_value = previous + current
        previous = current
        current = next_value

    return current
```

### Key Insight

To compute `F(n)`, we only need:

- `F(n−1)` (current)
- `F(n−2)` (previous)

This means:

- Only **two variables** are needed  
- Each Fibonacci number is computed **exactly once**  
- Time complexity becomes **O(n)**  
- Space complexity becomes **O(1)**  

This is dynamic programming in its simplest form.

# **Why Dynamic Programming Is Faster**

### Recursive Approach

- Recomputes the same values many times  
- Exponential time  
- Very slow for large `n`  

### Dynamic Programming Approach

- Stores and reuses results  
- Linear time  
- Efficient even for large `n`  

# **Comparison Table**

| Version | Behavior | Time Complexity | Space Complexity |
|--------|----------|-----------------|------------------|
| Recursive | Recomputes many values | Exponential | O(n) call stack |
| Dynamic Programming | Computes each value once | Linear | O(1) |

# **Why This Matters**

- Fibonacci clearly shows the difference between **naive recursion** and **dynamic programming**.  
- DP transforms an exponential-time algorithm into a linear-time one.  
- The DP version is practical for large inputs, while the recursive version becomes unusable.  
- This example introduces the core DP ideas used in more advanced problems.
