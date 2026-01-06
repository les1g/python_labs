# Here we have a list
my_list = [] # this is an empty list

#let's add numbers to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(2) # adding a duplicate value
my_list.append(8)

# print current list
print("Current List:", my_list)

# to see how lists work with removing elements 
my_list.remove(2) # removes the first occurrence of 2
print("List after removing first occurrence of 2:", my_list)

# you can also remove an element by its index
del my_list[2] # removes the element at index 2
print("List after removing element at index 2:", my_list)   

print("As you can see you do not need to shift elements manually when removing from a list.")

