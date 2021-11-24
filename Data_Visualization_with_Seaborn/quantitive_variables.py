import pandas as pd

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/student-alcohol-consumption.csv")
mpg = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/mpg.csv")
# -----------------------------------------------
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", kind="scatter", data=student_data)

# Show plot
plt.show()
# -----------------------------------------------
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter", col="study_time")

# Show plot
plt.show()
# -----------------------------------------------
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()
# -----------------------------------------------
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes", "no"])

# Show plot
plt.show()
# -----------------------------------------------
# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders",
            hue="cylinders")

# Show plot
plt.show()
# -----------------------------------------------
# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg",
            hue="origin",
            style="origin", data=mpg, kind="scatter")

# Show plot
plt.show()
# -----------------------------------------------
# Create line plot
sns.relplot(x="model_year", y="mpg", data=mpg, kind="line")

# Show plot
plt.show()
# -----------------------------------------------
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Show plot
plt.show()
# -----------------------------------------------
# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",
            dashes=False,
            markers=True)

# Show plot
plt.show()
# -----------------------------------------------