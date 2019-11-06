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

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city would you want to filter by? New York City, Chicago or Washington?\n").lower()
    #lower is used to get input in any format
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry, I didn't catch that. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhich month would you want to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n").lower()
    #lower is used to get input in any format
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, I didn't catch that. Please try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
    #lower is used to get input in any format
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, I didn't catch that. Please try again.")
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
    #load data file into a dataframe:
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    
    # extract month and day of week from Start Time to create new columns:
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable:
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe:
        df = df[df['month'] == month]

        # filter by day of week if applicable:
    if day != 'all':
        # filter by day of week to create the new dataframe:
        df = df[df['day_of_week'] == day.title()]

    print(df.head())
    #head is used to get first 5 rows
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].mode()[0]
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " and ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    time_1 = total_travel_time
    day = time_1 // (24 * 3600)
    time_1 = time_1 % (24 * 3600)
    hour = time_1 // 3600
    time_1 %= 3600
    minutes = time_1 // 60
    time_1 %= 60
    seconds = time_1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    time_2 = mean_travel_time
    day_2 = time_2 // (24 * 3600)
    time_2 = time_2 % (24 * 3600)
    hour_2 = time_2 // 3600
    time_2 %= 3600
    minutes_2 = time_2 // 60
    time_2 %= 60
    seconds_2 = time_2
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour_2, minutes_2, seconds_2))


    # display descriptive statistics for trip duration 

    descriptive_trip_duration = df['Trip Duration'].describe()
    print('\nDescriptive Statistics: {}'.format(descriptive_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    # print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

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


if __name__ == "__main__":
	main()