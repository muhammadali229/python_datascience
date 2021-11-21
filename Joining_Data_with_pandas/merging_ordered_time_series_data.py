import pandas as pd
from pandas import Timestamp
import matplotlib.pyplot as plt

sp500 = pd.read_csv(
    "D:/python_Data_Science/Joining_Data_with_pandas/S&P500.csv")
gdp = pd.read_csv(
    "D:/python_Data_Science/Joining_Data_with_pandas/WorldBank_GDP.csv")
pop = pd.read_csv(
    "D:/python_Data_Science/Joining_Data_with_pandas/WorldBank_POP.csv")

# -----------------------------------------------
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on="Year", right_on="date",
                             how="left")
# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(
    gdp, sp500, left_on="Year", right_on="date", how="left", fill_method="ffill")

# Print gdp_sp500
print(gdp_sp500)
# Subset the gdp and returns columns
gdp_returns = gdp_sp500[["GDP", "returns"]]

# Print gdp_returns correlation
print(gdp_returns.corr())
# -----------------------------------------------
unemployment = pd.DataFrame(data=[['2013-06-01', 7.5],
                                  ['2014-01-01', 6.7],
                                  ['2014-06-01', 6.1],
                                  ['2015-01-01', 5.6],
                                  ['2015-06-01', 5.3],
                                  ['2016-01-01', 5.0],
                                  ['2016-06-01', 4.9],
                                  ['2017-01-01', 4.7],
                                  ['2017-06-01', 4.3],
                                  ['2018-01-01', 4.1],
                                  ['2018-06-01', 4.0],
                                  ['2019-01-01', 3.9],
                                  ['2019-06-01', 3.7],
                                  ['2020-01-01', 3.5]],
                            columns=["date", "unemployment_rate"])
inflation = pd.DataFrame(data=[['2014-01-01', 235.28799999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-02-01', 235.547, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-03-01', 236.028, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-04-01', 236.468, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-05-01', 236.918, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-06-01', 237.231, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-07-01', 237.498, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-08-01', 237.46, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2014-09-01', 237.477, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-10-01', 237.43, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2014-11-01', 236.983, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2014-12-01', 236.252, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-01-01', 234.718, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-02-01', 235.236, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-03-01', 236.005, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-04-01', 236.15599999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-05-01', 236.97400000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-06-01', 237.68400000000003, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-07-01', 238.053, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-08-01', 238.028, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-09-01', 237.50599999999997, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-10-01', 237.78099999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-11-01', 238.016, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2015-12-01', 237.817, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-01-01', 237.833, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-02-01', 237.46900000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-03-01', 238.03799999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-04-01', 238.827, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-05-01', 239.46400000000003, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-06-01', 240.167, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-07-01', 240.15, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2016-08-01', 240.602, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-09-01', 241.051, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-10-01', 241.69099999999997, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-11-01', 242.02900000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2016-12-01', 242.77200000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-01-01', 243.78, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2017-02-01', 243.96099999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-03-01', 243.74900000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-04-01', 244.051, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-05-01', 243.96200000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-06-01', 244.18200000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-07-01', 244.39, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2017-08-01', 245.297, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-09-01', 246.418, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-10-01', 246.58700000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-11-01', 247.332, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2017-12-01', 247.90099999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-01-01', 248.88400000000001, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-02-01', 249.36900000000003, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-03-01', 249.498, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-04-01', 249.956, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-05-01', 250.646, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-06-01', 251.13400000000001, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-07-01', 251.597, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-08-01', 251.87900000000002, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-09-01', 252.01, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2018-10-01', 252.794, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX'],
                               ['2018-11-01', 252.76, 'CUSR0000SA0',
                                   'SEASONALLY ADJUSTED INDEX'],
                               ['2018-12-01', 252.72299999999998, 'CUSR0000SA0',
                                'SEASONALLY ADJUSTED INDEX']], columns=['date', 'cpi', 'seriesid', 'data_type'])
# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(
    inflation, unemployment, on="date", how="inner")

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x="unemployment_rate", y="cpi", kind="scatter")
plt.show()
# -----------------------------------------------
# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop,
                             on=["Year", "Country Name"],
                             fill_method='ffill')
# Print ctry_date
print(ctry_date.head())
# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop,
                             on=["Country Name", "Year"],
                             fill_method='ffill')

# Print date_ctry
print(date_ctry.head())
# -----------------------------------------------
jpm = pd.DataFrame(data=[[Timestamp('2017-11-17 15:35:17'), 98.12],
                         [Timestamp('2017-11-17 15:40:04'), 98.18],
                         [Timestamp('2017-11-17 15:45:01'), 97.7307],
                         [Timestamp('2017-11-17 15:50:55'), 97.74],
                         [Timestamp('2017-11-17 15:55:00'), 97.815],
                         [Timestamp('2017-11-17 16:00:30'), 98.02],
                         [Timestamp('2017-11-17 16:05:07'), 97.8],
                         [Timestamp('2017-11-17 16:10:08'), 97.84],
                         [Timestamp('2017-11-17 16:15:11'), 97.71],
                         [Timestamp('2017-11-17 16:20:29'), 97.76],
                         [Timestamp('2017-11-17 16:25:25'), 97.82],
                         [Timestamp('2017-11-17 16:30:53'), 97.95],
                         [Timestamp('2017-11-17 16:35:11'), 97.99],
                         [Timestamp('2017-11-17 16:40:44'), 98.06],
                         [Timestamp('2017-11-17 16:45:52'), 98.05],
                         [Timestamp('2017-11-17 16:50:37'), 98.1101],
                         [Timestamp('2017-11-17 16:55:02'), 98.18]], columns=['date_time', 'close'])
wells = pd.DataFrame(data=[[Timestamp('2017-11-17 15:35:08'), 54.3227],
                           [Timestamp('2017-11-17 15:40:00'), 54.32],
                           [Timestamp('2017-11-17 15:45:32'), 54.19],
                           [Timestamp('2017-11-17 15:50:07'), 54.17],
                           [Timestamp('2017-11-17 15:55:00'), 54.1841],
                           [Timestamp('2017-11-17 16:00:30'), 54.265],
                           [Timestamp('2017-11-17 16:05:52'), 54.2],
                           [Timestamp('2017-11-17 16:10:22'), 54.155],
                           [Timestamp('2017-11-17 16:15:43'), 54.19],
                           [Timestamp('2017-11-17 16:20:07'), 54.205],
                           [Timestamp('2017-11-17 16:25:13'), 54.23],
                           [Timestamp('2017-11-17 16:30:04'), 54.22],
                           [Timestamp('2017-11-17 16:35:32'), 54.22],
                           [Timestamp('2017-11-17 16:40:09'), 54.28],
                           [Timestamp('2017-11-17 16:45:24'), 54.24],
                           [Timestamp('2017-11-17 16:50:28'), 54.17],
                           [Timestamp('2017-11-17 16:55:42'), 54.18]], columns=['date_time', 'close'])
bac = pd.DataFrame(data=[[Timestamp('2017-11-17 15:35:17'), 26.552],
                         [Timestamp('2017-11-17 15:40:06'), 26.552],
                         [Timestamp('2017-11-17 15:45:05'), 26.388],
                         [Timestamp('2017-11-17 15:50:34'), 26.378],
                         [Timestamp('2017-11-17 15:55:06'),
                          26.383000000000003],
                         [Timestamp('2017-11-17 16:00:18'),
                          26.451999999999998],
                         [Timestamp('2017-11-17 16:05:20'), 26.373],
                         [Timestamp('2017-11-17 16:10:05'), 26.388],
                         [Timestamp('2017-11-17 16:15:07'), 26.369],
                         [Timestamp('2017-11-17 16:20:29'), 26.388],
                         [Timestamp('2017-11-17 16:25:00'), 26.467],
                         [Timestamp('2017-11-17 16:30:18'), 26.482],
                         [Timestamp('2017-11-17 16:35:08'),
                          26.491999999999997],
                         [Timestamp('2017-11-17 16:40:46'),
                          26.526999999999997],
                         [Timestamp('2017-11-17 16:45:55'), 26.522],
                         [Timestamp('2017-11-17 16:50:05'),
                          26.546999999999997],
                         [Timestamp('2017-11-17 16:55:02'), 26.566999999999997]], columns=['date_time', 'close'])
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time',
                              suffixes=('_jpm', '_bac'), direction='nearest')
print(jpm_wells_bac.head())
# Compute price diff
price_diffs = jpm_wells_bac.diff()
print(price_diffs.head())
# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()
# -----------------------------------------------
recession = pd.DataFrame(data=[[Timestamp('1980-01-01 00:00:00'), 'recession'],
                               [Timestamp('1980-08-01 00:00:00'), 'normal'],
                               [Timestamp('1981-07-01 00:00:00'), 'recession'],
                               [Timestamp('1982-12-01 00:00:00'), 'normal'],
                               [Timestamp('1990-07-01 00:00:00'), 'recession'],
                               [Timestamp('1991-04-01 00:00:00'), 'normal'],
                               [Timestamp('2001-03-01 00:00:00'), 'recession'],
                               [Timestamp('2001-12-01 00:00:00'), 'normal'],
                               [Timestamp('2007-12-01 00:00:00'), 'recession'],
                               [Timestamp('2009-07-01 00:00:00'), 'normal']], columns=['date', 'econ_status'])
gdp = pd.DataFrame(data=[[Timestamp('1979-01-01 00:00:00'), 2526.61],
                         [Timestamp('1979-04-01 00:00:00'),
                          2591.2470000000003],
                         [Timestamp('1979-07-01 00:00:00'), 2667.565],
                         [Timestamp('1979-10-01 00:00:00'), 2723.883],
                         [Timestamp('1980-01-01 00:00:00'), 2789.842],
                         [Timestamp('1980-04-01 00:00:00'),
                          2797.3520000000003],
                         [Timestamp('1980-07-01 00:00:00'),
                          2856.4829999999997],
                         [Timestamp('1980-10-01 00:00:00'),
                          2985.5570000000002],
                         [Timestamp('1981-01-01 00:00:00'),
                          3124.2059999999997],
                         [Timestamp('1981-04-01 00:00:00'), 3162.532],
                         [Timestamp('1981-07-01 00:00:00'),
                          3260.6090000000004],
                         [Timestamp('1981-10-01 00:00:00'),
                          3280.8179999999998],
                         [Timestamp('1982-01-01 00:00:00'), 3274.302],
                         [Timestamp('1982-04-01 00:00:00'), 3331.972],
                         [Timestamp('1982-07-01 00:00:00'), 3366.322],
                         [Timestamp('1982-10-01 00:00:00'),
                          3402.5609999999997],
                         [Timestamp('1983-01-01 00:00:00'), 3473.413],
                         [Timestamp('1983-04-01 00:00:00'), 3578.848],
                         [Timestamp('1983-07-01 00:00:00'), 3689.179],
                         [Timestamp('1983-10-01 00:00:00'),
                          3794.7059999999997],
                         [Timestamp('1984-01-01 00:00:00'), 3908.054],
                         [Timestamp('1984-04-01 00:00:00'),
                          4009.6009999999997],
                         [Timestamp('1984-07-01 00:00:00'), 4084.25],
                         [Timestamp('1984-10-01 00:00:00'), 4148.5509999999995]], columns=['date', 'gdp'])
# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on="date")

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s ==
                'recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()
# -----------------------------------------------
# Merge gdp and pop on date and country with fill
# gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# # Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
# gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# # Pivot data so gdp_per_capita, where index is date and columns is country
# gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# # Select dates equal to or greater than 1991-01-01
# recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# # Plot recent_gdp_pop
# recent_gdp_pop.plot(rot=90)
# plt.show()
# -----------------------------------------------
ur_wide = pd.DataFrame(data=[['2010', 9.8, 9.8, 9.9, 9.9, 9.6, 9.4, 9.4, 9.5, 9.5, 9.4, 9.8,
                              9.3],
                             ['2011', 9.1, 9.0, 9.0, 9.1, 9.0, 9.1, 9.0, 9.0, 9.0, 8.8, 8.6,
                              8.5],
                             ['2012', 8.3, 8.3, 8.2, 8.2, 8.2, 8.2, 8.2, 8.1, 7.8, 7.8, 7.7,
                              7.9],
                             ['2013', 8.0, 7.7, 7.5, 7.6, 7.5, 7.5, 7.3, 7.2, 7.2, 7.2, 6.9,
                              6.7],
                             ['2014', 6.6, 6.7, 6.7, 6.2, 6.3, 6.1, 6.2, 6.1, 5.9, 5.7, 5.8,
                              5.6],
                             ['2015', 5.7, 5.5, 5.4, 5.4, 5.6, 5.3, 5.2, 5.1, 5.0, 5.0, 5.1,
                              5.0],
                             ['2016', 4.9, 4.9, 5.0, 5.0, 4.8, 4.9, 4.8, 4.9, 5.0, 4.9, 4.7,
                              4.7],
                             ['2017', 4.7, 4.6, 4.4, 4.4, 4.4, 4.3, 4.3, 4.4, 4.2, 4.1, 4.2,
                              4.1],
                             ['2018', 4.1, 4.1, 4.0, 4.0, 3.8, 4.0, 3.8, 3.8, 3.7, 3.8, 3.7,
                              3.9],
                             ['2019', 4.0, 3.8, 3.8, 3.6, 3.6, 3.7, 3.7, 3.7, 3.5, 3.6, 3.5,
                              3.5],
                             ['2020', 3.6, 3.5, 4.4, float("nan"), float("nan"), float("nan"), float("nan"), float("nan"), float("nan"), float("nan"), float("nan"),
                              float("nan")]], columns=['year', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars=["year"], var_name="month", value_name="unempl_rate")


# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values("date")

# Plot the unempl_rate by date
ur_sorted.plot(x = "date", y="unempl_rate")
plt.show()
# -----------------------------------------------
# Use melt on ten_yr, unpivot everything besides the metric column
# bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# # Use query on bond_perc to select only the rows where metric=close
# bond_perc_close = bond_perc.query('metric == "close"')

# # Merge (ordered) dji and bond_perc_close on date with an inner join
# dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date', 
#                             suffixes=('_dow', '_bond'), how='inner')

# # Plot only the close_dow and close_bond columns
# dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
# plt.show()
# -----------------------------------------------