# read name of input file
input_file = input()

# range of search
lower_bound = input()
upper_bound = input()

# open, read, and close the input file
file = open(input_file)
file_contents = file.readlines()
file.close()

# print contents within range of bounds
for word in file_contents:
    # compares first letter of each word
    if lower_bound <= word.strip() <= upper_bound:
        print(word, end='')

