import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/movies.p")
financials = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/financials.p")
taglines = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/taglines.p")
movie_to_genres = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/movie_to_genres.p")
crews = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/crews.p")
ratings = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/ratings.p")
sequels = pd.read_pickle(
    "D:/python_Data_Science/Joining_Data_with_pandas/sequels.p")
# actors_movies = pd.read_pickle(
#     "D:/python_Data_Science/Joining_Data_with_pandas/sequels.p")
# -----------------------------------------------------
# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)
# -----------------------------------------------------
toy_story = movies[movies["title"].isin([
                   "Toy Story", "Toy Story 2", "Toy Story 3"])]
print(toy_story.head())
# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on="id", how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on="id")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
# -----------------------------------------------------
scifi_movies = movie_to_genres[movie_to_genres["genre"] == "Science Fiction"]
action_movies = movie_to_genres[movie_to_genres["genre"] == "Action"]
# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(
    scifi_only, left_on="id", right_on="movie_id")

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)
# -----------------------------------------------------
pop_movies = movies.sort_values("popularity", ascending=False)
# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on="movie_id", 
                                      right_on="id")

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()
# -----------------------------------------------------
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
# iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
#                                      on="id",
#                                      how="outer",
#                                      suffixes=("_1","_2"))

# # Create an index that returns true if name_1 or name_2 are null
# m = ((iron_1_and_2['name_1'].isnull()) | 
#      (iron_1_and_2['name_2'].isnull()))

# # Print the first few rows of iron_1_and_2
# print(iron_1_and_2[m].head())
# -----------------------------------------------------
# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())
# -----------------------------------------------------
# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on="id", how="left")

# Print the first few rows of movies_ratings
print(movies_ratings.head())
# -----------------------------------------------------
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", ascending=False).head())
# -----------------------------------------------------