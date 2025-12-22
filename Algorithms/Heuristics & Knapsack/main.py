from greedy_knapsack import greedy_knapsack
from optimized_Knapsack import optimal_knapsack

if __name__ == "__main__":

    print("\n================ EXAMPLE 1: Greedy is GOOD =================\n")

    # Greedy-friendly dataset
    items = [
        {"weight": 6, "value": 25},
        {"weight": 8, "value": 42},
        {"weight": 14, "value": 65},
        {"weight": 18, "value": 95},
        {"weight": 20, "value": 100},
    ]

    optimal = optimal_knapsack(items, 30)
    greedy = greedy_knapsack(items, 30)

    print("Optimal result (Example 1):")
    print(optimal, "\n")

    print("Greedy result (Example 1):")
    print(greedy, "\n")

    print("Explanation:")
    print("In this dataset, the highest-value items ALSO form the best combination.")
    print("Greedy picks the same items as the optimal algorithm because")
    print("no combination of smaller items can beat the value of {100 + 42}.\n")
    print("=> Greedy works well here because the data is simple and 'clean'.\n")


    print("\n================ EXAMPLE 2: Greedy FAILS =================\n")

    # Dataset where greedy fails
    items = [
        {"weight": 25, "value": 100},
        {"weight": 24, "value": 99},
        {"weight": 2,  "value": 40},
    ]

    optimal = optimal_knapsack(items, 26)
    greedy = greedy_knapsack(items, 26)

    print("Optimal result (Example 2):")
    print(optimal, "\n")

    print("Greedy result (Example 2):")
    print(greedy, "\n")

    print("Explanation:")
    print("Greedy chooses the highest-value item first (100),")
    print("but that leaves no room for anything else.")
    print("The optimal solution chooses items worth 99 + 40 = 139, which is MUCH better. \n")
    print("=> Greedy fails because it makes short-sighted decisions.\n")


    print("\n================ EXAMPLE 3: When to Use Each =================\n")

    # Larger dataset to show performance difference
    items = [
        {"weight": 10, "value": 60},
        {"weight": 20, "value": 100},
        {"weight": 30, "value": 120},
        {"weight": 5,  "value": 40},
        {"weight": 7,  "value": 50},
        {"weight": 3,  "value": 20},
    ]

    optimal = optimal_knapsack(items, 50)
    greedy = greedy_knapsack(items, 50)

    print("Optimal result (Example 3):")
    print(optimal, "\n")

    print("Greedy result (Example 3):")
    print(greedy, "\n")

    print("Explanation:")
    print("Both algorithms give reasonable answers, but optimal guarantees the best one.")
    print("Greedy is much faster and works well when:")
    print(" - You have many items")
    print(" - You need a quick estimate")
    print(" - Exact optimal value is not required")
    print("\nOptimal is better when:")
    print(" - Accuracy matters")
    print(" - You cannot afford to miss the best combination")
    print(" - The dataset is small enough for DP to run efficiently\n")