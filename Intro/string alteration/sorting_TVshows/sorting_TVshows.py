def read_file(file):
    """Takes file name as argument.
    Opens and reads file lines.
    Removes new line characters.
    Returns a list."""
    with open(file) as f: # open file
        file_contents = f.read().splitlines() # read and remove newlines
    return file_contents

def add_shows_and_seasons(file_contents):
    """Takes file contents as an argument.
    Adds file content season and shows as
    pairs to a dictionary.
    Returns a dictionary."""
    shows_and_seasons = {}
    for i in range(0, len(file_contents), 2):
        season = file_contents[i] + ':' # season
        show = file_contents[i + 1]     # show

        # add to dict
        shows_and_seasons.setdefault(season, []).append(show)
    return shows_and_seasons

def sort_shows_and_seasons(shows_and_seasons):
    """Sorts seasons with corresponding shows.
    Returns them as a new dictionary."""
    sorted_shows_seasons = {key: shows_and_seasons[key] for key in sorted(shows_and_seasons.keys())}
    return sorted_shows_seasons

def write_keys_to_file(sorted_content):
    """Takes dictionary as argument.
    Creates file and adds dict contents to file.
    Returns nothing."""
    with open('output_keys.txt', 'w') as keys_file:
        for key in sorted_content:
            for show in sorted_content[key]:
                if len(sorted_content[key]) > 1:
                    first_show = sorted_content[key][0]
                    second_show = sorted_content[key][1]
                    keys_file.write(f'{key} {first_show}; {second_show}\n')
                    break
                else:
                    keys_file.write(f'{key} {show}\n')

def write_values_to_files(sorted_content):
    """Takes dictionary as argument.
    Sorts dict values in alpha order.
    Creates file and adds dict contents to file.
    Returns nothing"""
    sorted_shows = sorted(sorted_content.values())
    with open('output_titles.txt', 'w') as titles_file:
        for show in sorted_shows:
            for i in show:
                titles_file.write(f'{i} \n')

input_file = input().strip()

# read the file store contents
contents = read_file(input_file)

# add file contents to a dict
contents = add_shows_and_seasons(contents)

# sort the contents of the dict
sorted_contents = sort_shows_and_seasons(contents)

# write sorted contents to a new file
write_keys_to_file(sorted_contents)

# write sorted values to a new file
write_values_to_files(sorted_contents)
