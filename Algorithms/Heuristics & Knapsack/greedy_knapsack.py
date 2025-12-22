def greedy_knapsack(items, capacity):
    """
    Heuristic: Always take the highest-value item that fits.
    items = list of dicts: {"weight": w, "value": v}
    capacity = max weight allowed
    """
    # Sort items by value descending
    items_sorted = sorted(items, key=lambda x: x["value"], reverse=True)

    total_value = 0
    total_weight = 0
    chosen_items = []

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

