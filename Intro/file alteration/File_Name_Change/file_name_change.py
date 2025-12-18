# collect input
photo_file_names = input().strip()

# read file
with open(photo_file_names, 'r') as file_names:
    file_names_list = file_names.readlines() # store file contents as a list

# modify file
for name in file_names_list:
    # handle edge case when file is empty
    if name == '\n':
        print('Nothing to modify.', end='')
    new_txt_file = name.replace('_photo.jpg', '_info.txt') # replace file name
    # put modified file name to output
    print(new_txt_file, end='')