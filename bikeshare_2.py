''' 
	 Abdelmenam tarek abdelmenam
	created :- 9-12-2020
	data track professional project 1
	" bike share "
'''
# i used pycharm
# in line 91 i used dt.day_name() instead of dt.weekday_name
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

 # function 1 ......................................................................
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # lists that have the valid input
    cities = [ 'chicago' , 'new york city' , 'washington' ]
    monthes = [ 'all' , 'january' , 'february' , 'march' , 'april' , 'may' , 'june' ]
    days = [ 'monday' , 'tuesday' , 'wednesday' ,  'thursday' , 'friday' , 'saturday' , 'sunday' , 'all' ]

    print("Hello! Let's explore some US bikeshare data! \n ")

    while True :
        # get user input for city
        city = input("Would you like to see data for Chicago, New York city, or Washington? ").lower()
        # get user input for city (chicago, new york city, washington).
        if city in cities  :
            answer = input("you choose {} , are you sure 'yes' or 'no' ?".format(city))
            if answer.lower() == 'yes' :
                break
        else :
            print("invalid input try again ... ")
            print("make sure that you choose from here " , cities)

    while True:
        # get user input for month (all, january, february, ... , june)
        month = input("Which month - January, February, March, April, May, or June? ").lower()
        if month in monthes :
            break
        else:
            print("invalid input try again ... ")
            print("make sure that you choose from here ", monthes)

    while True:
         # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").lower()
        if day in days:
            break
        else:
            print("invalid input try again ... ")
            print("make sure that you choose from here ", days)

    print('-'*40)
    return city, month, day


#function 2 ..........................................................................
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

    # convring start time from string format to date format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting monthes in new column Month
    df['Month'] = df['Start Time'].dt.month
    # extracting the day in new column Day Name
    df['Day Name'] = df['Start Time'].dt.day_name() #i used dt.day_name() instead of dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[:][df['Month'] == month]

    if day != 'all':
        # update the data frame by the day
        df = df[:][df['Day Name'] == day.title()]

    return df


#function 3 .................................................................
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    # extracting starting hour from start time date
    df['Start hour'] = df['Start Time'].dt.hour

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['Month'].mode()[0]
    print("the most common month is ", months[most_common_month-1])
    print("  with total number of counts " , df['Month'][df['Month'] == most_common_month].count())

    # display the most common day of week
    most_common_day = df['Day Name'].mode()[0]
    print("the most common day of week  is ", most_common_day)
    print("  with total number of counts " , df['Day Name'][df['Day Name'] == most_common_day].count())

    # display the most common start hour
    most_common_hour = df['Start hour'].mode()[0]
    print("the most common start hour is ", most_common_hour )
    print("  with total number of counts " , df['Start hour'][df['Start hour'] == most_common_hour].count())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#function 4 ..................................................................
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most common start station is' , df['Start Station'].mode()[0] )

    # display most commonly used end station
    print('the most common end station is' , df['End Station'].mode()[0] )

    # creat new column with the combination between the two column
    df['Start And End Station Combination'] = df['Start Station'] + ',' + df['End Station']
    common_station = df['Start And End Station Combination'].mode()[0].split(',')
    # display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip is ')
    print("start station : {} . end station : {}".format(common_station[0], common_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#function 5.....................................................................
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("the total travel time is {} seconds".format(df['Trip Duration'].sum()))

    # display mean travel time
    print("he average travel time is {} seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#function 6 .......................................................
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("toatal number of user types is \n", df['User Type'].value_counts())

    # using try ecxept becuse washington tale doesn't has gendeer and birth year table
    try:
        # Display counts of gender
        print("toatal number of genders is \n", df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        # minimum
        print("the earliest birth of birth is ", df['Birth Year'].min())
        # muximum
        print("the most recent birth of birth is ", df['Birth Year'].max())
        # common
        print("the most most common birth of birth is ", df['Birth Year'].mode()[0])
    except:
        print("you choose washington table and it doesn't has gender band date of birth column")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#function 7 "extra option from me " .................................
def show_random_sample(df):
    '''
    function to dispaly a random sample to the user
    argument :- data frame to show a saomple from it
    return : it doesn't return but it print
    '''

    while True:
        answer = input("would you like to see random sample ? 'yes' for accept / else for refuse ").lower()
        if answer == 'yes':
            random_number = np.random.randint(0,df['Start Time'].count())
            print(df.iloc[random_number] )
        else :
            print("you refuse to see random sample")
            break

# main function which will be run
def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_random_sample(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
