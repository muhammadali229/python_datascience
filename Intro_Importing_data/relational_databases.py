from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
# ----------------------------------------------
engine = create_engine(
    'mssql://@HAIER-PC\DATA_ANALYST/Northwind?driver=SQL+Server+Native+Client+11.0')
con = engine.connect()
print(pd.read_sql_query('SELECT * FROM Orders', con))
con.close()
# ----------------------------------------------
insp = inspect(engine)
table_names = insp.get_table_names()
print(table_names)
# ----------------------------------------------
# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Customers')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
print(df.head())
# Close connection
con.close()
# ----------------------------------------------
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employees')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
# ----------------------------------------------

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employees WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())
# ----------------------------------------------
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employees ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())
# ----------------------------------------------
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employees', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employees")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))
# ----------------------------------------------
# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    'SELECT * FROM Employees WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())
# ----------------------------------------------
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Customers.LastName FROM Customers INNER JOIN Employees ON Employees.EmployeeID = Customers.EmployeeID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
# ----------------------------------------------
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
# ----------------------------------------------