import os
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'netflix_titles.csv')

df = pd.read_csv(
    file_path, 
    encoding='utf-8-sig', 
    on_bad_lines='skip', 
    engine='python'
)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())

print(df.isnull().sum())
print(df.isnull().sum().sum())

print(df["type"].value_counts())

print(df["release_year"].describe())

print(df["rating"].value_counts())

print(df["type"].value_counts())

print(df["country"].value_counts().head(10))

print(df["director"].value_counts().head(10))

print(df["listed_in"].value_counts().head(10))

df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

df["country"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

df["rating"].value_counts().head(10).plot(kind="bar")

plt.title("Content Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

df["listed_in"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("top_10_genres.png")
plt.show()