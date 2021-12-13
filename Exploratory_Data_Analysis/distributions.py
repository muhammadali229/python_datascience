import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from empyrical_dist import Pmf, Cdf
from scipy.stats import norm
gss = pd.read_hdf(
    'D:/python_Data_Science/Exploratory_Data_Analysis/gss.hdf5', 'gss')
# --------------------------------------------
# Compute the PMF for year
pmf_year = Pmf.from_seq(gss['year'], normalize=False)

# Print the result
print(pmf_year)
# --------------------------------------------
# Select the age column
age = gss['age']

# Make a PMF of age
pmf_age = Pmf.from_seq(age)

# Plot the PMF
pmf_age.bar()

# Label the axes
plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()
# --------------------------------------------
# Select the age column
age = gss['age']

# Compute the CDF of age
cdf_age = Cdf.from_seq(age)

# Calculate the CDF of 30
print(cdf_age[30])
# --------------------------------------------
income = gss['realinc']

cdf_income = Cdf.from_seq(income)

# Calculate the 75th percentile
percentile_75th = cdf_income.inverse(0.75)

# Calculate the 25th percentile
percentile_25th = cdf_income.inverse(0.25)

# Calculate the interquartile range
iqr = percentile_75th - percentile_25th

# Print the interquartile range
print(iqr)
# --------------------------------------------
# Select realinc
income = gss['realinc']

# Make the CDF
cdf_income = Cdf.from_seq(income)

# Plot it
cdf_income.plot()

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()
# --------------------------------------------
educ = gss['educ']
cdf_educ = Cdf.from_seq(educ)
print(cdf_educ[12])
cdf_educ.plot()
# Label the axes
plt.xlabel('Education levels')
plt.ylabel('CDF')
plt.show()
plt.close()
# --------------------------------------------
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = ((educ >= 14) & (educ < 16))

# High school (12 or fewer years of education)
high = (educ <= 12)
print(high.mean())
# --------------------------------------------
income = gss['realinc']

# Plot the CDFs
Cdf.from_seq(income[high]).plot(label='High school')
Cdf.from_seq(income[assc]).plot(label='Associate')
Cdf.from_seq(income[bach]).plot(label='Bachelor')

# Label the axes
plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()
# --------------------------------------------
# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)
print('Log10 of income: {}'.format(log_income))
# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print('log_income mean: {} and std: {}'
      .format(mean, std))

dist = norm(mean, std)
# --------------------------------------------
# Evaluate the model CDF
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

# Plot the model CDF
plt.clf()
plt.plot(xs, ys, color='gray')

# Create and plot the Cdf of log_income
Cdf.from_seq(log_income).plot()
    
# Label the axes
plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()
# --------------------------------------------