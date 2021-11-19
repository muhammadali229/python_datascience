import pandas as pd
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

avocados = pd.read_pickle(
    "D:/python_Data_Science/Data_manipulation_with_pandas/avoplotto.pkl")

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()
# --------------------------------------------
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
print(nb_sold_by_date)
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()
# --------------------------------------------
# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price",
              title="Number of avocados sold vs. average price",
              kind="scatter")

# Show the plot
plt.show()
# --------------------------------------------
# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(
    alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
# --------------------------------------------
avocados_2016 = avocados.loc[(avocados["date"] >=
                              "2016-01-01") & (avocados["date"] <= "2016-12-31")]
print(avocados_2016)

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()
# --------------------------------------------
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
# --------------------------------------------
# print(avocados.columns)
# # From previous step
# cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# avocados_2016[cols_with_missing].hist()
# plt.show()

# # Fill in missing values with 0
# avocados_filled = avocados_2016.fillna(0)

# # Create histograms of the filled columns
# avocados_filled[cols_with_missing].hist()

# # Show the plot
# plt.show()
# --------------------------------------------
# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
# --------------------------------------------
# Create a dictionary of lists with new data
avocados_dict = {
    "date": ["2019-11-17", "2019-12-01"],
    "small_sold": [10859987, 9291631],
    "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)
# --------------------------------------------
airlines_data = [['DELTA AIR LINES', 2017, 679, 99796155],
                 ['VIRGIN AMERICA', 2017, 165, 6090029],
                 ['JETBLUE AIRWAYS', 2017, 1475, 27255038],
                 ['UNITED AIRLINES', 2017, 2067, 70030765],
                 ['HAWAIIAN AIRLINES', 2017, 92, 8422734],
                 ['EXPRESSJET AIRLINES', 2017, 785, 11738812],
                 ['SKYWEST AIRLINES', 2017, 917, 24516354],
                 ['AMERICAN AIRLINES', 2017, 4517, 98017132],
                 ['ALASKA AIRLINES', 2017, 658, 18817924],
                 ['SOUTHWEST AIRLINES', 2017, 6678, 115988988],
                 ['FRONTIER AIRLINES', 2017, 540, 12059943],
                 ['SPIRIT AIRLINES', 2017, 1502, 17069647],
                 ['DELTA AIR LINES', 2016, 912, 97237060],
                 ['VIRGIN AMERICA', 2016, 77, 5927938],
                 ['JETBLUE AIRWAYS', 2016, 2140, 25990828],
                 ['UNITED AIRLINES', 2016, 2874, 64438132],
                 ['HAWAIIAN AIRLINES', 2016, 30, 8154838],
                 ['EXPRESSJET AIRLINES', 2016, 2541, 16119866],
                 ['SKYWEST AIRLINES', 2016, 2177, 22575383],
                 ['AMERICAN AIRLINES', 2016, 6598, 99348093],
                 ['ALASKA AIRLINES', 2016, 734, 17725197],
                 ['SOUTHWEST AIRLINES', 2016, 11907, 112153048],
                 ['FRONTIER AIRLINES', 2016, 688, 10895052],
                 ['SPIRIT AIRLINES', 2016, 1418, 15234924]]
airline_bumping = pd.DataFrame(airlines_data, columns=[
                               'airline', 'year', 'nb_bumped', 'total_passengers'])
# From previous steps
print(airline_bumping.head())
airline_totals = airline_bumping.groupby(
    "airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / \
    airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)
# --------------------------------------------
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values(
    "bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv(
    "D:/python_Data_Science/Data_manipulation_with_pandas/airline_totals_sorted.csv")
# --------------------------------------------
