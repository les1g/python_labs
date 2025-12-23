from greedy_Fractional_Knapsack import Item, fractional_knapsack

# Example usage:
if __name__ == "__main__":
    # ------------------------------------------------------------
    # 1. Create a list of items.
    # Each item has: (name, value, weight)
    #
    # The greedy algorithm will compute each item's value-to-weight
    # ratio and sort them from highest to lowest.
    # ------------------------------------------------------------
    items = [
        Item("Gold", 60, 10),     # ratio = 6.0
        Item("Silver", 100, 20),  # ratio = 5.0
        Item("Bronze", 120, 30),  # ratio = 4.0
    ]
    # ------------------------------------------------------------
    # 2. Set the knapsack capacity.
    #
    # The algorithm will take whole items while they fit.
    # When an item no longer fits completely, it will take only
    # the fraction that fits.
    # ------------------------------------------------------------
    capacity = 50
    # ------------------------------------------------------------
    # 3. Run the greedy fractional knapsack algorithm.
    #
    # Returns:
    # - total_value: the maximum value achievable with fractions allowed
    # - result_items: the list of items with updated `.fraction` values
    # ------------------------------------------------------------
    total_value, result_items = fractional_knapsack(items, capacity)
    # ------------------------------------------------------------
    # 4. Display results.
    #
    # Each item will show how much of it was taken (fraction 0.0–1.0).
    # ------------------------------------------------------------
    print("Total value in knapsack:", total_value)
    print("\nItems taken (with fractions):")

    for item in result_items:
        print(f"- {item.name}: "
              f"value={item.value}, "
              f"weight={item.weight}, "
              f"fraction_taken={item.fraction:.2f}")