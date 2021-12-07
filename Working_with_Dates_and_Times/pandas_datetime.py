# Import pandas
import pandas as pd
# Import matplotlib
import matplotlib.pyplot as plt

# Load CSV into the rides variable
rides = pd.read_csv('D:/python_Data_Science/Working_with_Dates_and_Times/capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])
# -----------------------------------------------------------
# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())
# -----------------------------------------------------------
# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds"
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds"
      .format(rides[joyrides]['Duration'].median()))
# -----------------------------------------------------------
# Resample rides to daily, take the size, plot the results
rides.resample('D', on='Start date')\
    .size()\
    .plot(ylim=[0, 15])

# Show the results
plt.show()

# Import matplotlib

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date')\
    .size()\
    .plot(ylim=[0, 150])

# Show the results
plt.show()
# -----------------------------------------------------------
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())
# -----------------------------------------------------------
# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type')\
    .resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())
# -----------------------------------------------------------
# Localize the Start date column to America/New_York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York',
                                                         ambiguous='NaT')
# Print first value
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')

# Print the new value
print(rides['Start date'].iloc[0])
# -----------------------------------------------------------
# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())
# -----------------------------------------------------------