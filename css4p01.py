# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:35:39 2024

@author: Luwy Swanepoel
"""
# Luwy Swanepoel
# 34200894
# CSS Project - Option 1: IMDB Data

# STEP 1 LOAD DATA
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
 
# STEP 2 CLEAN DATA
# REMOVE REDUNDANT INDEX
df = pd.read_csv("movie_dataset.csv",index_col=0)
# NEW COLUMN NAMES
df.rename(columns={'Runtime (Minutes)':'Runtime_Minutes'}, inplace=True)
df.rename(columns={'Revenue (Millions)':'Revenue_Millions'}, inplace=True)
# REPLACE NANS OR EMPTY CELLS WITH AVERAGE
x = df["Revenue_Millions"].mean()
df["Revenue_Millions"].fillna(x, inplace=True)
y = df["Metascore"].mean()
df["Metascore"].fillna(y, inplace=True)
# REMOVE DUPLICATES 
df.drop_duplicates(inplace=True)

# QUESTION 1: HIGHEST RATED MOVIE = THE DARK KNIGHT
print(df['Rating'].max())
print(df[df['Rating']==9.0])

# QUESTION 2: AVERAGE REVENUE = 83 MILLION
print(df['Revenue_Millions'].mean())

# QUESTION 3: AVERAGE REVENUE FROM 2015-2017 = 68 MILLION
rr = df[(df['Year']>=2015)&(df['Year']<=2017)]
print(rr['Revenue_Millions'].mean())

# QUESTION 4: AMOUNT OF MOVIES IN 2016 = 297
yd = (df[df['Year']==2016])
print(yd['Year'].count())

# QUESTION 5: MOVIES DIRECTED BY CHRISTOPHER NOLAN = 5
options = ['Christopher Nolan']
cn = df[df['Director'].isin(options)]
print(cn['Director'].count())

# QUESTION 6: RATING OF AT LEAST 8 (>8) = 78
mr = df[(df['Rating']>=8)]
print(mr['Rating'].count())

# QUESTION 7: MEDIAN OF CHRISTOPHER NOLAN MOVIES = 8.6
options = ['Christopher Nolan']
mnc = df[df['Director'].isin(options)]
print(mnc['Rating'].median())

# QUESTION 8: YEAR WITH HIGHEST AVERAGE RATING = 2007
grouped = df.groupby('Year')
avg_rating = grouped['Rating'].mean()
print(avg_rating)

# QUESTION 9: PERCENTAGE INCREASE IN MOVIES FROM 2006-2016 = 575
pii = (df[df['Year']==2006])
print(pii['Year'].count())
pif = (df[df['Year']==2016])
print(pif['Year'].count())
initial = 44
final = 297
pc = (final-initial)/initial*100
print(pc)

# QUESTION 10: MOST COMMON ACTOR = Mark Wahlberg
df[['Actor1','Actor2','Actor3','Actor4']]=df['Actors'].str.split(',',expand=True)
df1 = df['Actor1'].str.strip()
df2 = df['Actor2'].str.strip()
df3 = df['Actor3'].str.strip()
df4 = df['Actor4'].str.strip()
df5 = pd.concat([df1, df2, df3, df4], ignore_index=True)
print(df5.mode())
value_counts_actors = df5.value_counts()
print(value_counts_actors)

# QUESTION 11: HOW MANY UNIQUE GENRES = 20
df[['Genre1','Genre2','Genre3']]=df['Genre'].str.split(',',expand=True)
df21 = df['Genre1'].str.strip()
df22 = df['Genre2'].str.strip()
df23 = df['Genre3'].str.strip()
df24 = pd.concat([df21, df22, df23], ignore_index=True)
value_counts_genres = df24.value_counts()
print(value_counts_genres)
print(value_counts_genres.count())

# QUESTION 12: 5 INSIGHTS TO PRODUCE BETTER MOVIES
# Top 10 Genres With Respect To Rating
grouped = df.groupby('Genre')
avg_genre_rating = grouped['Rating'].mean()
avg_genre_rating_top_ten = avg_genre_rating.sort_values(ascending=False)
print(avg_genre_rating_top_ten[0:10])
# Top 10 Genres With Respect To Revenue
grouped = df.groupby('Genre')
avg_genre_revenue = grouped['Revenue_Millions'].mean()
avg_genre_revenue_top_ten = avg_genre_revenue.sort_values(ascending=False)
print(avg_genre_revenue_top_ten[0:10])
# Top 10 Directors With Respect To Revenue
grouped = df.groupby('Director')
avg_director_revenue = grouped['Revenue_Millions'].mean()
avg_director_revenue_top_ten = avg_director_revenue.sort_values(ascending=False)
print(avg_director_revenue_top_ten[0:10])
# Top 10 Directors With Respect To Rating
grouped = df.groupby('Director')
avg_director_rating = grouped['Rating'].mean()
avg_director_rating_top_ten = avg_director_rating.sort_values(ascending=False)
print(avg_director_rating_top_ten[0:10])
# Top 10 Best Runtimes With Respect To Rating
grouped = df.groupby('Runtime_Minutes')
avg_runtime_rating = grouped['Rating'].mean()
avg_runtime_rating_top_ten = avg_runtime_rating.sort_values(ascending=False)
print(avg_runtime_rating_top_ten[0:10])
# Top 10 Best Actor Combinations With Respect To Rating
grouped = df.groupby('Actors')
avg_actors_rating = grouped['Rating'].mean()
avg_actors_rating_top_ten = avg_actors_rating.sort_values(ascending=False)
print(avg_actors_rating_top_ten[0:10])
# Correlation Table
df.corr()

