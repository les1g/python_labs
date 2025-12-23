"""
This module contains the classic recursive Fibonacci implementation.

Key characteristics:
- Uses direct recursion.
- Each call branches into two more calls.
- Recomputes many values.
- Exponential time complexity.
"""

def recursive_fibonacci(n):
    """Compute Fibonacci number using plain recursion."""
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)