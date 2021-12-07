# Import date from datetime
from datetime import datetime, timedelta, timezone
import pandas as pd
# Import tz
from dateutil import tz

onebike = pd.read_csv(
    'D:/python_Data_Science/Working_with_Dates_and_Times/capital-onebike.csv')
onebike_datetimes = onebike[['Start date', 'End date']].to_dict('records')
# ---------------------------------------------------
# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())
# ---------------------------------------------------
# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['Start date'] = pd.to_datetime(trip['Start date']).replace(tzinfo=edt)
    trip['End date'] = pd.to_datetime(trip['End date']).replace(tzinfo=edt)
# ---------------------------------------------------
# Loop over the trips
for trip in onebike_datetimes[:10]:
    # Pull out the start
    dt = pd.to_datetime(trip['Start date'])
    # Move dt to be in UTC
    dt = dt.astimezone(timezone.utc)

    # Print the start time in UTC
    print('Original:', trip['Start date'], '| UTC:', dt.isoformat())
# ---------------------------------------------------
# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['Start date'] = pd.to_datetime(trip['Start date']).replace(tzinfo=et)
    trip['End date'] = pd.to_datetime(trip['End date']).replace(tzinfo=et)
# ---------------------------------------------------
# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = pd.to_datetime(onebike_datetimes[0]['Start date'])

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = pd.to_datetime(onebike_datetimes[0]['Start date'])

# What time was it in India?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = pd.to_datetime(onebike_datetimes[0]['Start date'])

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())
# ---------------------------------------------------
# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo=tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc))
      .total_seconds()/(60*60))
# ---------------------------------------------------
# Create starting date
dt = datetime(2000, 3, 29, tzinfo=tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
    print(dt.replace(year=y).isoformat())
# ---------------------------------------------------
# Loop over trips
for trip in onebike_datetimes:
    # Rides with ambiguous start
    if tz.datetime_ambiguous(pd.to_datetime(trip['Start date']), tz=timezone.utc):
        print("Ambiguous start at " + str(trip['Start date']))
    # Rides with ambiguous end
    if tz.datetime_ambiguous(pd.to_datetime(trip['End date']), tz=timezone.utc):
        print("Ambiguous end at " + str(trip['End date']))
# ---------------------------------------------------
trip_durations = []
for trip in onebike_datetimes:
  trip['Start date'] = pd.to_datetime(trip['Start date'])
  trip['End date'] = pd.to_datetime(trip['End date'])
  # When the start is later than the end, set the fold to be 1
  if trip['Start date'] > trip['Start date']:
    trip['End date'] = tz.enfold(trip['End date'])
  # Convert to UTC
  start = trip['Start date'].replace(tzinfo=tz.UTC)
  end = trip['End date'].replace(tzinfo=tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))
# ---------------------------------------------------