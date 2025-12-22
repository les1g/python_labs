# Heuristics & The Knapsack Problem

## Goal of this module

Understand how heuristics provide **fast, approximate solutions** to complex optimization problems like the knapsack problem.  

This module demonstrates:
- What heuristics are
- Why optimal solutions can be too slow
- How a greedy heuristic works for the 0‑1 knapsack problem
- The trade-offs between optimal and heuristic approaches

## What is a Heuristic?
A heuristic is a strategy that:
- Accepts a non-optimal solution
- Runs significantly faster
- Uses fewer computational resources

Heuristics are widely used in:
- AI
- Robotics
- Route planning
- Scheduling
- Optimization problems

## The Knapsack Problem
Given items with weights and values, and a knapsack with a weight limit, choose items that maximize total value without exceeding the limit.

This problem is **NP-complete**, meaning the number of combinations grows exponentially.

Finding the perfect (optimal) solution can be slow for large inputs.

## Heuristic Solution (Greedy)
A simple heuristic for the 0‑1 knapsack problem:
> Always take the most valuable item that fits in the remaining space.

This approach:
- Is fast
- Is easy to implement
- Does not guarantee the optimal solution

The greedy method works well in many cases but fails when a combination of smaller items beats a single high‑value item.

## Optimal Solution
The optimal 0‑1 knapsack solution uses dynamic programming:
> Explore all combinations efficiently using a DP table to guarantee the maximum possible value.

This approach:
- Always finds the optimal solution
- Handles all item combinations correctly
- Is slower than the heuristic (O(n × capacity))
- Uses more memory

Dynamic programming is the gold standard when accuracy matters more than speed.

## 📚 Why this matters
This module teaches:
- How heuristics trade accuracy for speed
- Why some problems cannot be solved optimally in reasonable time
- How greedy algorithms work in practice
- How to evaluate algorithmic trade‑offs
- When to choose heuristic vs optimal approaches

Understanding both methods helps you design algorithms that balance performance and accuracy depending on the problem.

