# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt
import pandas as pd

seattle_weather = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Matplotlib/seattle_weather.csv")
austin_weather = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Matplotlib/austin_weather.csv")
summer_2016_medals = pd.read_csv(
    "D:/python_Data_Science/Data_Visualization_with_Matplotlib/summer2016.csv")
# -------------------------------------------------------
# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()
# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()
fig.set_size_inches([5, 5])
# Save as a PNG file with 300 dpi
fig.savefig(
    "D:/python_Data_Science/Data_Visualization_with_Matplotlib/my_figure_300dpi.png", dpi=300)
# -------------------------------------------------------
# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)
# -------------------------------------------------------
fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
    # Extract the rows only for this sport
    sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
    # Add a bar for the "Weight" mean with std y error bar
    ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)
fig.set_size_inches([20, 15])
# Save the figure to file
fig.savefig(
    "D:/python_Data_Science/Data_Visualization_with_Matplotlib/sports_weights.png")
# -------------------------------------------------------
