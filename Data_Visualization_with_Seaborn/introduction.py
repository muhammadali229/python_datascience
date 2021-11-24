import pandas as pd

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


countries = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/countries-of-the-world.csv")

gdp = countries["GDP ($ per capita)"].tolist()
phones = countries["Phones (per 1000)"].tolist()
percent_literate = countries["Literacy (%)"].tolist()
region = countries["Region"].tolist()
# -----------------------------------------------
# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()
# -----------------------------------------------
# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
# -----------------------------------------------
df = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/young-people-survey-responses.csv")
print(df.head())

# Create a count plot with "Spiders" on the x-axis
sns.countplot("Spiders", data=df)

# Display the plot
plt.show()
# -----------------------------------------------
student_data = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/student-alcohol-consumption.csv")

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", data=student_data,
                hue="location", hue_order=["Rural", "Urban"])

# Show plot
plt.show()
# -----------------------------------------------
# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x = "school", data=student_data, hue="location", palette=palette_colors)

# Display plot
plt.show()
# -----------------------------------------------





# -----------------------------------------------