from find_top_five import display_top_five_salespersons

if __name__ == "__main__":
    print("\n=== Top Five Salespersons Demo ===\n")
    print("This example shows how the algorithm maintains a fixed-size")
    print("array of the top five performers, updating it as new data arrives.\n")

    all_salespersons = [
        {"name": "Alice", "salesTotal": 120},
        {"name": "Bob", "salesTotal": 95},
        {"name": "Carol", "salesTotal": 300},
        {"name": "Dan", "salesTotal": 150},
        {"name": "Eve", "salesTotal": 200},
    ]

    print("Input sales data:")
    for sp in all_salespersons:
        print(f"  {sp['name']}: {sp['salesTotal']}")

    print("\nProcessing and displaying the top five...\n")
    display_top_five_salespersons(all_salespersons)

    print("\nNote:")
    print("- The array always stays sorted in descending order.")
    print("- Only five entries are kept, even if more data is provided.")
    print("- This mirrors real-world leaderboard and ranking systems.\n")
