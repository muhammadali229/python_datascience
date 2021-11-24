import pandas as pd

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Import median function from numpy
from numpy import median

survey_data = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/young-people-survey-responses.csv")
student_data = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Seaborn/student-alcohol-consumption.csv")
# -------------------------------------------------
# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")
# Show plot
plt.show()
# -------------------------------------------------
survey_data["Interested in Math"] = [True if score ==
                                     5.0 else False for score in survey_data['Mathematics']]
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender", y="Interested in Math", kind="bar", data=survey_data)

# Show plot
plt.show()
# -------------------------------------------------
# List of categories from lowest to highest
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None)

# Show plot
plt.show()
# -------------------------------------------------
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3", data=student_data,
            kind="box",
            order=study_time_order)

# Show plot
plt.show()
# -------------------------------------------------
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", data=student_data, kind="box", hue="location",
            sym="")

# Show plot
plt.show()
# -------------------------------------------------
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box", whis=0.5)

# Show plot
plt.show()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()
# -------------------------------------------------
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            join=False,	data=student_data,
            kind="point",
            capsize=0.2)

# Show plot
plt.show()
# -------------------------------------------------
# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None, estimator=median)

# Show plot
plt.show()
# -------------------------------------------------