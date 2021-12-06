import pandas as pd
import datetime as dt

ride_sharing_new = pd.read_csv(
    "D:/python_Data_Science/Cleaning_data/ride_sharing_new.csv")
# -------------------------------------
# Print the information of ride_sharing
print(ride_sharing_new.info())

# Print summary statistics of user_type column
print(ride_sharing_new['user_type'].describe())

# Convert user_type from integer to category
ride_sharing_new['user_type_cat'] = ride_sharing_new['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing_new['user_type_cat'].dtype == 'category'

# Print new summary statistics
print(ride_sharing_new['user_type_cat'].describe())
# -------------------------------------
# Strip duration of minutes
ride_sharing_new['duration_trim'] = ride_sharing_new['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing_new['duration_time'] = ride_sharing_new['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing_new['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration
print(ride_sharing_new[['duration', 'duration_trim', 'duration_time']])
print(ride_sharing_new['duration_time'].mean())
# -------------------------------------
ride_sharing = pd.read_csv(
    "D:/python_Data_Science/Cleaning_data/ride_sharing.csv")
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())
# -------------------------------------
# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())
# -------------------------------------
# Find duplicates
duplicates = ride_sharing.duplicated(subset=['ride_id'], keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])
# -------------------------------------
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)

duplicated_rides = ride_unique[duplicates == True]
# print(duplicated_rides)
# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
# -------------------------------------