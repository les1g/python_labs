# Fractional Knapsack Problem (Greedy Algorithm)

## Overview

The **fractional knapsack problem** is a classic optimization problem where you aim to maximize the total value placed into a knapsack with limited capacity.  

Unlike the 0‑1 knapsack problem, **items can be split**, allowing the greedy strategy to produce an optimal solution.

This implementation uses:

- **Value‑to‑weight ratio sorting**
- **Greedy selection**
- **Fractional item inclusion when necessary**

## Why Greedy Works Perfectly

Greedy is optimal here because:

- Items can be divided into fractions.
- Taking the item with the **highest value per unit weight** always increases total value as fast as possible.
- No combination of lower‑ratio items can outperform taking the highest‑ratio item first.

This property is known as the **Greedy Choice Property**.

## Algorithm Steps

1. Compute each item's **value‑to‑weight ratio**.
2. Sort items by ratio in **descending** order.
3. Take whole items while they fit.
4. When the next item doesn’t fully fit:
   - Take the **fraction** that fits.
5. Stop when the knapsack is full.

## Time Complexity

| Operation | Cost |
|----------|------|
| Sorting items | \(O(n \log n)\) |
| Single pass through items | \(O(n)\) |
| **Total** | **\(O(n \log n)\)** |

## Code Structure

### `Item` Class
- Stores `name`, `value`, `weight`
- Computes `ratio` (value/weight)
- Tracks `fraction` taken

### `fractional_knapsack()` Function
- Sorts items by ratio
- Greedily fills the knapsack
- Returns:
  - `total_value`
  - list of items with updated `.fraction`

## Example Output

```
Total value in knapsack: 240.0
Items taken:
Gold: value=60, weight=10, fraction=1.00
Silver: value=100, weight=20, fraction=1.00
Bronze: value=120, weight=30, fraction=0.67
```

## When to Use This Algorithm

Use fractional knapsack when:

- Items **can be split**
- You need a **fast**, **optimal** solution
- Value‑to‑weight ratio meaningfully represents item quality

Do **not** use this for 0‑1 knapsack — greedy fails there.

## Summary

- Greedy is **optimal** for fractional knapsack.
- The algorithm is simple, fast, and mathematically justified.
- This repo provides a clean, educational implementation suitable for coursework, interviews, and teaching.