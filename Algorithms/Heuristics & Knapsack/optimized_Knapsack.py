def optimal_knapsack(items, capacity):
    """
    Optimal 0-1 Knapsack using Dynamic Programming.
    items = list of dicts: {"weight": w, "value": v}
    capacity = max weight allowed
    """

    n = len(items)

    # DP table: (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        weight = items[i - 1]["weight"]
        value = items[i - 1]["value"]

        for w in range(1, capacity + 1):
            if weight <= w:
                # Option 1: take the item
                take = value + dp[i - 1][w - weight]
                # Option 2: skip the item
                skip = dp[i - 1][w]
                dp[i][w] = max(take, skip)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find chosen items
    chosen_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item was taken
            chosen_items.append(items[i - 1])
            w -= items[i - 1]["weight"]

    total_value = dp[n][capacity]
    total_weight = sum(item["weight"] for item in chosen_items)

    return {
        "items": chosen_items[::-1],  # reverse to original order
        "total_weight": total_weight,
        "total_value": total_value
    }
