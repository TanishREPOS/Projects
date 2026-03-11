# NETFLIX DATA ANALYSIS PROJECT #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

df = pd.read_csv("netflix_titles.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# data cleaining stage #

df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)
df['duration'].fillna('Unknown', inplace=True)

# Changing the date column #
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# removing redundency if any #
df.drop_duplicates(inplace=True)


# Visual representation between Movies vs TV Shows #
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.show()


#Top 10 Countries that are Producing Content #
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()


# Content Release Trend #
plt.figure(figsize=(12,6))
df['release_year'].value_counts().sort_index().plot(kind='line')
plt.title("Netflix Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()


# Ratings of the Content Distribution #
plt.figure(figsize=(10,6))
sns.countplot(y='rating', data=df, order=df['rating'].value_counts().index)
plt.title("Distribution of Netflix Content Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.show()


# Genres Analysis #
genres = df['listed_in'].str.split(',', expand=True).stack()

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.show()


# Top Directors of the movies or Tv shows # 
top_directors = df['director'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_directors.values, y=top_directors.index)
plt.title("Top Directors with Most Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.show()



# Movie Duration Analysis #
movies = df[df['type'] == 'Movie']

movies['duration'] = movies['duration'].str.replace(' min','')
movies['duration'] = pd.to_numeric(movies['duration'], errors='coerce')

plt.figure(figsize=(10,6))
sns.histplot(movies['duration'].dropna(), bins=30)
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()
