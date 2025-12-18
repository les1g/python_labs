# contact name and number
contact_book = {
}

# split into substrings at each space
add_contacts = input().split()

# add name and number to contact book
for name in add_contacts:
    name, number = name.split(',')
    contact_book[name] = number

# find name in contact book and print their number
find_name = input().strip().title()
print(contact_book[find_name])
