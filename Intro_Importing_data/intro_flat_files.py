import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# ----------------------------------------------
# Open a file: file
file = open('D:/python_Data_Science/Intro_Importing_data/moby_dick.txt', mode='r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
# ----------------------------------------------
# Read & print the first 3 lines
with open('D:/python_Data_Science/Intro_Importing_data/moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
# ----------------------------------------------
# Assign filename to variable: file
file = 'D:/python_Data_Science/Intro_Importing_data/digits.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))
# ----------------------------------------------
# Assign filename: file
file = 'D:/python_Data_Science/Intro_Importing_data/seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
# ----------------------------------------------
file = 'D:/python_Data_Science/Intro_Importing_data/titanic_sub.csv'
data = np.genfromtxt(file,
                     delimiter=',', names=True, dtype=None)
print(np.shape(data))
print(data['Survived'])
# ----------------------------------------------
# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
# ----------------------------------------------
# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
# ----------------------------------------------
# Assign filename to variable: file
file = 'D:/python_Data_Science/Intro_Importing_data/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))
# ----------------------------------------------
# Assign filename to variable: file
file = 'D:/python_Data_Science/Intro_Importing_data/titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
# ----------------------------------------------