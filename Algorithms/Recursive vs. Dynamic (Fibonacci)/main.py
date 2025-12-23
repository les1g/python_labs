"""
Main program that imports both Fibonacci implementations and demonstrates
the difference between recursive and dynamic programming approaches.

This file explains:
- What dynamic programming is.
- Why recursion is slow for Fibonacci.
- Why the dynamic version is efficient.
"""

from recursive_solution import recursive_fibonacci
from dynamic_solution import dynamic_fibonacci

def explain():
    print("\n=== Fibonacci Comparison ===\n")
    print("Dynamic programming is a technique where:")
    print("1. A problem is broken into smaller subproblems.")
    print("2. Subproblem results are stored.")
    print("3. Stored results are reused to avoid recomputation.\n")

    print("Fibonacci is a classic example.\n")
    print("Recursive version:")
    print("- Uses plain recursion.")
    print("- Recomputes many values.")
    print("- Exponential time.\n")

    print("Dynamic programming version:")
    print("- Stores only the previous two terms.")
    print("- Computes each Fibonacci number once.")
    print("- Linear time.\n")

def main():
    explain()

    n = 10
    print(f"Computing Fibonacci({n}) using both methods...\n")

    # Dynamic programming result
    dp_result = dynamic_fibonacci(n)
    print(f"Dynamic programming result: {dp_result}")

    # Recursive result
    rec_result = recursive_fibonacci(n)
    print(f"Recursive result:          {rec_result}")

    print("\nBoth produce the same answer, but the dynamic version is far more efficient.")
    print("Try increasing n to see how quickly the recursive version slows down.")

if __name__ == "__main__":
    main()