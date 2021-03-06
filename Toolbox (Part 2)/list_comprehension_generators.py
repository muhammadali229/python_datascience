import pandas as pd
# -----------------------------------------------
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
print([doc[0] for doc in doctor])
# -----------------------------------------------
# Create list comprehension: squares
squares = [i * i for i in range(0, 10)]
print(squares)
# -----------------------------------------------
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)
# -----------------------------------------------
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]

# Print the new list
print(new_fellowship)
# -----------------------------------------------
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)
# -----------------------------------------------
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry',
              'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
# -----------------------------------------------
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
# -----------------------------------------------
# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths

def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)


# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)
# -----------------------------------------------
df = pd.read_csv('D:/python_Data_Science/Toolbox (Part 2)/tweets.csv',
            encoding="ISO-8859-1")
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)
# -----------------------------------------------
# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11: 19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
# -----------------------------------------------