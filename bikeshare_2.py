import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city not in CITY_DATA:
            print("Error! Please try again. Enter the correct city (chicago, new york city,washington).")
            continue
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWould you like to filter the data for all, January, February, ..., or June?\n").lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Error! Please try again. Enter the correct month or all.")
            continue
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWould you like the day filtered by all, Monday, Tuesday, ..., or Sunday?\n").lower()
        if day not in ('all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Error! Please try again. Enter the correct day or all.")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month:", common_month, '\n')



    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day of week:", common_day, '\n')


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour:", common_hour, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    used_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station:", used_start_station, '\n')


    # display most commonly used end station
    used_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:", used_end_station, '\n')


    # display most frequent combination of start station and end station trip
    start_to_end = df['Start Station'] + " / " + df['End Station']
    dict_count = start_to_end.value_counts().to_dict()
    freq_comb = max(dict_count, key=dict_count.get)
    print("The most frequent combination of start to end station trip:", freq_comb, '\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    if 'Trip Duration' in df:
    # display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print("The total travel time:", total_travel_time, '\n')

    # display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print("The mean travel time:", mean_travel_time, '\n')
    else:
        print('Trip Duration stats cannot be calculated because Trip Duration does not appear in the dataframe\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df:
        counts_user_types = df['User Type'].value_counts()
        print("Counts of user types:", counts_user_types, '\n')
    else:
        print("User Type stats cannot be calculated because User Type does not appear in the dataframe\n")

    # Display counts of gender
    if 'Gender' in df:
        counts_gender = df['Gender'].value_counts()
        print("Counts of Gender:", counts_gender, '\n')
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe\n') 


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print("The earliest year of birth:", earliest_year, '\n')

        most_recent = df['Birth Year'].max()
        print("The most recent year of birth:", most_recent, '\n')

        birth_year_count = df['Birth Year'].value_counts()
        dict_count = birth_year_count.to_dict()
        common_year = max(dict_count, key=dict_count.get)
        print("The most common year of birth:", common_year, '\n')
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no:\n").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("\nDo you wish to continue? Enter yes or no:\n").lower()
        if view_display != 'yes':
            break


if __name__ == "__main__":
    main()
