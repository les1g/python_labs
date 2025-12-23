def greedy_knapsack(items, capacity):
    """
    0-1 Knapsack Problem using Heuristic strategy (Greedy Algorithm). 
    The algorithm always takes the highest-value item that fits.
    items = list of dicts: {"weight": w, "value": v}
    capacity = max weight allowed
    """
    # Sort items by value in descending order
    # This ensures we always consider the most valuable items first
    items_sorted = sorted(items, key=lambda x: x["value"], reverse=True)

    total_value = 0
    total_weight = 0
    chosen_items = []

    # Greedily add items while there's capacity
    # This may not yield the optimal solution
    # but is faster and simpler
    for item in items_sorted:
        if total_weight + item["weight"] <= capacity:
            chosen_items.append(item)
            total_weight += item["weight"]
            total_value += item["value"]

    return {
        "items": chosen_items,
        "total_weight": total_weight,
        "total_value": total_value
    }

