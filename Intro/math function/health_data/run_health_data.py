def health_data():
    """------------------------------------------------------
    The following calculates a user's age in days, minutes,
    seconds, amount of times user has sneezed, amount of
    times users heart has beat, number of calories user
    has expended, number of burgers equal that number of
    calories.
    """
    print(health_data.__doc__)

    user_age_years = int(input('enter your age in years:\n'))
    user_age_days = user_age_years * 365
    print(f'You are at least {user_age_days} days old.')

    # Calculates the user's age in minutes and seconds.
    user_age_hour = user_age_days * 24
    user_age_minutes = user_age_hour * 60
    user_age_seconds = user_age_minutes * 60
    print(f'You are at least {user_age_minutes} minutes old.')
    print(f'You are at least {user_age_seconds} seconds old.')

    # Calculates the user's amount of sneezes in lifetime.
    sneezes_per_day = 3
    user_sneezes = user_age_days * sneezes_per_day
    print(f'You have sneezed at least {user_sneezes} times.')

    # Calculates the times user's heart has beat.
    heart_beat_per_minute = 72
    user_total_heart_beats = user_age_minutes * heart_beat_per_minute
    print(f'Your heart has beat at least {user_total_heart_beats} times.')

    # calculates user's expended calories
    daily_calories = 2200
    user_total_calories = user_age_days * daily_calories
    print(f'You have expended at least {user_total_calories} calories.')

    # calculates number of food items total to calories
    cheese_burger_calories = 500
    total_burgers = user_total_calories / cheese_burger_calories
    print(f'You could have eaten at least {total_burgers} burgers with that amount.')
    print('------------------------------------------------------')