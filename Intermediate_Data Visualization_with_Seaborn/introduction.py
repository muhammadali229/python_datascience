# import all modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

grant_file = 'D:/python_Data_Science/Intermediate_Data Visualization_with_Seaborn/schoolimprovement2010grants.csv'

# Read in the DataFrame
df = pd.read_csv(grant_file)
# --------------------------------------------------
# Display pandas histogram
df['Award_Amount'].plot.hist()
plt.show()

# Clear out the pandas histogram
plt.clf()

# Display a Seaborn distplot
sns.distplot(df['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()
# --------------------------------------------------
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()
# --------------------------------------------------
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade': True})

# Plot the results
plt.show()
# --------------------------------------------------
insurance_premiums = 'D:/python_Data_Science/Intermediate_Data Visualization_with_Seaborn/insurance_premiums.csv'

# Read in the DataFrame
df = pd.read_csv(insurance_premiums)

# Create a regression plot of premiums vs. insurance_losses
sns.regplot(x='insurance_losses', y='premiums', data=df)

# Display the plot
plt.show()

# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(x='insurance_losses', y='premiums', data=df)

# Display the plot
plt.show()
# --------------------------------------------------
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()
# --------------------------------------------------
# Create a regression plot with multiple rows
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           row="Region")

# Show the plot
plt.show()
# --------------------------------------------------