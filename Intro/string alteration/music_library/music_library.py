music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

def get_artist_info():
    """Prints all artist names alphabetically, followed
    by their albums and details."""
    print(f'\nYou are viewing the music library\n---------------------------------')
    sorted_artists = sorted(music.keys())  # Sort artist names A-Z
    for artist in sorted_artists:
        print(f'Artist: {artist}')
        if music[artist]:
            sorted_albums = sorted(music[artist].keys())  # Sort albums A-Z
            for album in sorted_albums:
                album_details = music[artist][album]
                print(f"  Album: {album}")
                print(f"    Songs: {', '.join(album_details['songs'])}")
                print(f"    Year: {album_details['year']}")
                print(f"    Platinum: {'Yes' if album_details['platinum'] else 'No'}")
        else:
            print('No albums have been added yet.')
        print()  # Add a blank line between artists

def add_artist():
    """Adds an artist to music library"""
    print(f'You are adding an artist\n------------------------')
    artist = input('Artist: ').strip().title()
    if artist not in music: # handles duplicates
        music[artist] = {} # adds artist with no albums
        print(f'Adding artist "{artist}"...')
        print(f'Artist "{artist}" has been added to the music library.\n')
    else:
        print(f'Artist "{artist}" has already been added.')

def add_album():
    """Adds album to existing artist"""
    print(f'You are adding an album\n-----------------------')
    artist = input('Artist name: ').strip().title()
    album = input('Album name: ').strip().title()

    # check if artist is in music
    if artist in music:
        # adds album with empty details
        music[artist][album] = {
    'songs': [],
    'year': 0,
    'platinum': False
}
        print(f'Adding album "{album}" for artist "{artist}".')
        print(f'Album "{album}" has been added.')
    else:
        print(f'Failed to add the album "{album}" because artist "{artist}" was not found.\n'
              f'Add artist "{artist}" to library first.\n')

def add_song():
    """Adds song to existing album."""
    print(f'You are adding a song\n---------------------')
    artist = input('Artist name: ').strip().title()
    album = input('Album name: ').strip().title()
    song = input('Song name: ').strip().title()

    # check if artist is in music
    if artist in music:
        # check if album exists for artist
        if album in music[artist]:
            # add song to album song list
            music[artist][album]['songs'].append(song)
            print(f'Adding "{song}" by "{artist}" to "{album}".')
            print(f'"{song}" has been added.')
        else:
            print(f'Album "{album}" not found for artist "{artist}"')
            print(f'Add album "{album}" to library first.')

    else:
        print(f'Artist "{artist}" not found in the music library.')
        print(f'Add artist "{artist}" to library first.')


menu_prompt = (f'{"Menu":^22}\n'
               '----------------------\n'
               '(1) Add an artist\n' 
               '(2) Add an album\n' 
               '(3) Add a song\n' 
               '(4) View library\n'
               '(5) Exit\n'
               'Enter your selection: '
               )

# Get user input
menu_choice = input(menu_prompt).strip()

while menu_choice:
    if menu_choice == '5': # exit message
        print('Ending program. Goodbye.', end='')
        break
    elif menu_choice == '1': # Add an artist
        add_artist()
        menu_choice = input(menu_prompt).strip()
    elif menu_choice == '2': # Add an album
        add_album()
        menu_choice = input(menu_prompt).strip()
    elif menu_choice == '3': # Add a song
        add_song()
        menu_choice = input(menu_prompt).strip()
    elif menu_choice == '4': # View library
        get_artist_info()
        menu_choice = input(menu_prompt).strip()
    else: # handle incorrect menu choice
        print(f'Menu choice \'{menu_choice}\' is invalid. Please try again.\n')
        menu_choice = input(menu_prompt).strip()

