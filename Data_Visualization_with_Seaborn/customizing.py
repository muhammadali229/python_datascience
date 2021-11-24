import pandas as pd

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

survey_data = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/young-people-survey-responses.csv")
mpg = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/mpg.csv")
# -------------------------------------------------
# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()
# -------------------------------------------------
# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Siblings", y="Loneliness",
            data=survey_data, kind="bar")

# Show plot
plt.show()
# -------------------------------------------------
# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
custom_palette=["#39A7D0", "#36ADA4"]

sns.set_palette(custom_palette)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()
# -------------------------------------------------
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)
# -------------------------------------------------
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()
# -------------------------------------------------
mpg_mean = mpg.copy()
mpg_mean["mpg_mean"] = mpg["mpg"].mean() 
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels

g.set(xlabel="Car Model Year", ylabel="Average MPG")

# Show plot
plt.show()
# -------------------------------------------------
# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()
# -------------------------------------------------
survey_data["Interested in Pets"] = ['Yes' if score ==
                                     5.0 else 'No' for score in survey_data['Pets']]
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()
# -------------------------------------------------
# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()
# -------------------------------------------------