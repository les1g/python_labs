def display_top_five_salespersons(all_salespersons):
    # Create a list with 5 placeholder entries
    top_sales = [
        {"name": "", "salesTotal": -1},
        {"name": "", "salesTotal": -1},
        {"name": "", "salesTotal": -1},
        {"name": "", "salesTotal": -1},
        {"name": "", "salesTotal": -1},
    ]

    # Process each salesperson
    for sales_person in all_salespersons:

        # Check if this salesperson beats the current lowest top-five entry
        if sales_person["salesTotal"] > top_sales[-1]["salesTotal"]:

            # Replace the lowest entry
            top_sales[-1]["name"] = sales_person["name"]
            top_sales[-1]["salesTotal"] = sales_person["salesTotal"]

            # Sort from highest to lowest sales
            top_sales.sort(key=lambda x: x["salesTotal"], reverse=True)

    # Display the final top five
    for entry in top_sales:
        print(entry)