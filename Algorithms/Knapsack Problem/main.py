def Knapsack01(knapsack, itemList):
    # sort itemList descending by value
    # remaining = knapsack.maximumWeight
    remaining = knapsack
    
    for i in range(len(itemList)):
        if itemList[i]['weight'] <= remaining:
            # Put itemList[i] in knapsack
            remaining -= itemList[i]['weight']
        else:
            break
    return remaining

if __name__ == "__main__":
    knapsack = 50
    itemList = [
        {'value': 60, 'weight': 10},
        {'value': 100, 'weight': 20},
        {'value': 120, 'weight': 30},
    ]
    
    # Sort items by value-to-weight ratio in descending order
    itemList.sort(key=lambda x: x['value'] / x['weight'], reverse=True)

    print("Remaining weight in knapsack:", Knapsack01(knapsack, itemList))