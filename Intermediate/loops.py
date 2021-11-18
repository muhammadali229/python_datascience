import numpy as np
import pandas as pd
x = 1
while x < 4:
    print(x)
    x = x + 1

# ---------------------------------------------
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# ---------------------------------------------
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for v in areas:
    print(v)

# ---------------------------------------------
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for x, y in enumerate(areas):
    print("room" + str(x) + ":" + str(y))

# ---------------------------------------------
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas):
    print("room " + str(index + 1) + ": " + str(area))

# ---------------------------------------------
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for h in house:
    print("the " + h[0] + " is " + str(h[1]) + " sqm")

# ---------------------------------------------
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print("the capital of " + k + " is " + v)

# ---------------------------------------------
# For loop over np_height
# for x in np.nditer(np_height):
#     print(str(x) + " inches")

# # For loop over np_baseball
# for x in np.nditer(np_baseball):
#     print(x)

# ---------------------------------------------
cars = pd.read_csv('D:/python_Data_Science/Intermediate/cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# ---------------------------------------------
# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
    
# ---------------------------------------------
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

print(cars)

# ---------------------------------------------
cars['COUNTRY'] = cars['country'].apply(str.upper)

print(cars)