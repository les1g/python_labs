"""
This module contains the dynamic programming (iterative) Fibonacci implementation.

Key characteristics:
- Stores only the previous two terms.
- Each Fibonacci number is computed exactly once.
- Linear time complexity.
- Demonstrates dynamic programming: store and reuse results.
"""

def dynamic_fibonacci(n):
    """Compute Fibonacci number using dynamic programming (iterative)."""
    if n == 0:
        return 0

    previous = 0
    current = 1

    for _ in range(1, n):
        next_value = previous + current
        previous = current
        current = next_value

    return current