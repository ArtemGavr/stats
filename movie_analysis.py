# import csv
#
# with open('tmdb_5000_movies.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for line in csv_reader:
#         print(line)

import pandas
import matplotlib
import numpy as np
import heapq
import seaborn as sns
import matplotlib.pyplot as plt
import json

df = pandas.read_csv('tmdb_5000_movies.csv')
print(df['genres'][0])

genres_array = []
genres_length = 0
for i in df['genres']:
    dict_ids = json.loads(i)
    for g in dict_ids:
        genres_array.append((g['id'], g['name']))

# plotting all number params
dataset = pandas.DataFrame(df)
fig = plt.figure(figsize=(8, 8))
ax = fig.gca()
dataset.hist(ax=ax)
plt.show()

# plotting nit number params
def frequency_word(df, column):
    res = {}
    for i, row in df.iterrows():
        for item in row[column]:
            if item in res:
                res[item] += 1
            else:
                res[item] = 1
    return res

def to_list(item, key='name'):
  return[x[key] for x in eval(item)]

movies = pandas.read_csv('tmdb_5000_movies.csv')

movies.genres = movies.genres.apply(to_list)

genres = frequency_word(movies, 'genres')
top_genres = dict(sorted(genres.items()))
top_genres

ax = sns.barplot(list(top_genres.keys()), list(top_genres.values()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, fontsize=8, ha='right')
ax.set_title('Genres bar graph:')
plt.show()

movies.production_companies= movies.production_companies.apply(to_list)
produccomp = frequency_word(movies, 'production_companies')
top_produccomp = dict(sorted(produccomp.items())[:20])
top_produccomp

ax = sns.barplot(list(top_produccomp.keys()), list(top_produccomp.values()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=8, ha='right')
ax.set_title('Production companies bar graph:')
plt.show()

movies.production_countries = movies.production_countries.apply(to_list)
produccount = frequency_word(movies, 'production_countries')
top_produccount = dict(sorted(produccount.items())[:20])
top_produccount

ax = sns.barplot(list(top_produccount.keys()), list(top_produccount.values()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=10)
ax.set_title('Production countries bar graph:')
plt.show()

# counting weighted rating
min_my = 10 ** 10
for i in df['vote_count']:
    if i < min_my:
        min_my = i

counter = 0
sum_my = 0
for i in df['vote_average']:
    sum_my += i
    counter += 1

c = sum_my / counter  # aver vote count
new_rating = [0] * len(df['title'])
mappa = [df['title'].to_list(), new_rating] # arrays of 
for n in df['title']:
    ser = df['title'].to_list()
    index = ser.index(n)  # index of the current title
    r = df['vote_average'][index]
    v = df['vote_count'][index]
    if v == 0 and min_my == 0:
        mappa[1][index] = 0
    else:
        mappa[1][index] = (v * r / (v + min_my)) + (min_my * c / (v + min_my))

top10_ratings = [(-1, -1)]*10  # index value

for n in range(0, len(mappa[1])):
    for i in range(0, len(top10_ratings)):
        if mappa[1][n] > top10_ratings[i][1]:
            top10_ratings[i] = (n, mappa[1][n])  # index: rating_value pair
            break

top10_films = []
for i in top10_ratings:
    name = mappa[0][i[0]]
    top10_films.append((name, i[1]))

print('Top 10 movies: ', top10_films)
