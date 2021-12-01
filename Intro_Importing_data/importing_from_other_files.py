import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sas7bdat import SAS7BDAT
import h5py
import scipy.io
# ----------------------------------------------
# import os
# wd = os.getcwd()
# print(os.listdir(wd))
# ----------------------------------------------
# Assign filename to variable: file
file = 'D:/python_Data_Science/Intro_Importing_data/casts.p'

# Open pickle file and load data: d
with open(file, 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
# ----------------------------------------------
# Assign spreadsheet filename: file
file = 'D:/python_Data_Science/Intro_Importing_data/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)
# ----------------------------------------------
# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
# ----------------------------------------------
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=1, names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols='A', skiprows=1, names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
# ----------------------------------------------
# Save file to a DataFrame: df_sas
with SAS7BDAT('D:/python_Data_Science/Intro_Importing_data/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
# ----------------------------------------------
# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('D:/python_Data_Science/Intro_Importing_data/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
# ----------------------------------------------
# Assign filename: file
file = 'D:/python_Data_Science/Intro_Importing_data/LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
# ----------------------------------------------
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'][:10]

print(strain)
# ----------------------------------------------
# Load MATLAB file: mat
mat = scipy.io.loadmat(
    'D:/python_Data_Science/Intro_Importing_data/albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
# ----------------------------------------------
# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()