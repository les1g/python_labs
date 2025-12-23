# This code implements the Greedy Fractional Knapsack algorithm.

# Each item has a name, value, weight, and a fraction indicating how much of it is taken.
# The algorithm sorts items by their value-to-weight ratio and fills the knapsack
# to maximize total value, allowing for fractional items.
class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight
        self.fraction = 1.0  # default: take whole item

    @property
    def ratio(self):
        return self.value / self.weight

    def __repr__(self):
        return f"{self.name}: value={self.value}, weight={self.weight}, fraction={self.fraction:.2f}"

# The greedy fractional knapsack algorithm.
# It takes a list of items and the knapsack capacity,
# and returns the maximum value achievable and the list of items with their fractions taken.
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio (descending)
    items = sorted(items, key=lambda item: item.ratio, reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for item in items:
        if remaining_capacity == 0:
            break

        if item.weight <= remaining_capacity:
            # Take the whole item
            total_value += item.value
            remaining_capacity -= item.weight
            item.fraction = 1.0
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / item.weight
            item.fraction = fraction
            total_value += item.value * fraction
            remaining_capacity = 0

    return total_value, items