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
    print('\nHello! Let\'s explore some bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to     handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? \n').lower()
        if city in ['chicago', 'new york city', 'washington', 'all']:
            break
        else:
            print('\nInvalid city name. Please try again.\n')
            
    while True:
        month = input('\nWhich month would you like to see data for? \n').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('\nInvalid month name. Please try again.\n')
 
    while True:
        day = input('\nWhich day would you like to see data for? \n').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('\nInvalid day name. Please try again.\n')

    print('-'*40)
    return city, month, day
    city,month, day = get_filters()
  

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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

    df= load_data(city,month,day)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('The most common month is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('The most common day of the week is:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stations = df['Start Station'].value_counts()

    print("The most commonly used start station is: ", start_stations.idxmax())

    # TO DO: display most commonly used end station
    end_stations = df['End Station'].value_counts()

    print("The most commonly used end station is: ", end_stations.idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    station_combinations = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')

# Sort the combinations by count and display the most frequent combination
    most_frequent_combination = station_combinations.sort_values(by='count', ascending=False).iloc[0]
    print("The most frequent combination of start station and end station is: ")
    print("Start Station: ", most_frequent_combination['Start Station'])
    print("End Station: ", most_frequent_combination['End Station'])
    print("Count: ", most_frequent_combination['count'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Count of Gender:' , gender_counts)
    except KeyError:
        print('NOTE: No gender data recorded for Washington!')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]

        print("The earliest birth year is: ", earliest_birth_year)
        print("The most recent birth year is: ", most_recent_birth_year)
        print("The most common birth year is: ", most_common_birth_year)
    except KeyError:
        print('NOTE: No birth year data recorded for Washington!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0 
    while True:   
        view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no?\n")
        if view_data in 'yes':
                print(df.iloc[start_loc:start_loc+5]) 
                start_loc += 5
        elif view_data in 'no':
            break
        else:
            print('\nInvalid entry, try again.\n')
     
            view_display = input("Do you wish to continue?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()