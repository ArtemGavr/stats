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
import math
import seaborn as sns
import matplotlib.pyplot as plt
import json

df = pandas.read_csv("lab1\\tmdb_5000_movies.csv")


def medium_value(array):
    my_sum = 0
    for i in array:
        my_sum += i
    answer = my_sum / len(array)
    return answer


def dispersion(array):
    my_sum = 0
    for i in array:
        my_sum += i
    med = medium_value(array)

    answer = 0
    for i in array:
        answer += (i - med) ** 2
    answer = answer / len(array)
    return answer


def median(array):
    if len(array) % 2 == 1:
        index = len(array) // 2 + 1
        return array[index - 1]
    else:
        index = len(array) // 2 - 1  # -1 because array indexing
        return (array[index + 1] + array[index]) / 2


def moda(array):
    mappa_vhozdeni = dict.fromkeys(array, 0)
    for i in array:
        mappa_vhozdeni[i] += 1

    max_of_usages = -1
    moda_set = []
    for k, v in mappa_vhozdeni.items():
        if v > max_of_usages:
            max_of_usages = v
            moda_set = [k]
        elif v == max_of_usages:
            moda_set.append(k)

    if len(moda_set) == 2:
        array.sort()
        index_f = array.index(moda_set[0])
        index_s = array.index(moda_set[1])
        if (index_f + mappa_vhozdeni[moda_set[0]] - 1) == (index_s - 1):
            return [(moda_set[0] + moda_set[1]) / 2]

    return moda_set


def max_min(array):
    max_my = -1
    min_my = 10 ** 15
    for i in array:
        if i > max_my:
            max_my = i
        if i < min_my:
            min_my = i

    return max_my, min_my


def vidhilennya(disp):
    vidh = math.sqrt(disp)
    return vidh


# my_set = [5, 5, 5, 1, 2, 3, 4, 6, 6, 6, 7, 8, 9]
#
#
# print(moda(my_set))

my_set = df['popularity'].to_list()
print(f"{medium_value(my_set)} - medium value")

# дисперсия функции
print("Dispersion ", np.var(my_set))
disp = np.var(my_set)
print(f"{vidhilennya(disp)} - standartne vidhilennya")
print(f"{median(my_set)} - median")
print(f"{moda(my_set)} - moda/ modas")
print(f"{max_min(my_set)} - max/ min")
m_m = max_min(my_set)
print(f"{m_m[0] - m_m[1]} - rozmax")
print(" quantile 0.1 : ", np.quantile(my_set, .1))
print(" quantile 0.25 : ", np.quantile(my_set, .25))
print(" quantile 0.5 : ", np.quantile(my_set, .5))
print(" quantile 0.75 : ", np.quantile(my_set, .75))


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
ax.set_title('Genres:')
plt.show()

movies.production_companies= movies.production_companies.apply(to_list)
produccomp = frequency_word(movies, 'production_companies')
top_produccomp = dict(sorted(produccomp.items())[:20])
top_produccomp

ax = sns.barplot(list(top_produccomp.keys()), list(top_produccomp.values()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=8, ha='right')
ax.set_title('Production companies:')
plt.show()

movies.production_countries = movies.production_countries.apply(to_list)
produccount = frequency_word(movies, 'production_countries')
top_produccount = dict(sorted(produccount.items())[:20])
top_produccount

ax = sns.barplot(list(top_produccount.keys()), list(top_produccount.values()))
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=10)
ax.set_title('Production countries:')
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

movies_filtered = movies.loc[movies.vote_count != 0]
v = movies_filtered.vote_count
m = movies_filtered.vote_count.min()
r = movies_filtered.vote_average
c = movies_filtered.vote_average.mean()

weighted_rating = (v * r + m * c) / (v + m)
movies['weighted_rating'] = weighted_rating

top_movies = movies.sort_values(by='weighted_rating', ascending = False)
(top_movies.loc[:, ['title', 'weighted_rating']].head(10))

print('\n!!!!!!!!!!!!!!!!!top by genre!!!!!!!!!!!!!!!\n')

for genre in genres.keys():
  print(genre)
  indx = top_movies.genres.apply(lambda x: genre in x)
  print(top_movies.loc[indx, ['title', 'weighted_rating']].head(5))
  print('\n')


# median used for recounting
median = movies_filtered.vote_average.median()
weighted_rating_2 = (v * r + m * median) / (v + m)
movies['weighted_rating_2'] = weighted_rating_2

print('\n!!!!!!!!!!!!median for recounting top 10!!!!!!!!!!\n')
top_movies_2 = movies.sort_values(by='weighted_rating_2', ascending=False)
print(top_movies_2.loc[:, ['title', 'weighted_rating_2']].head(10))

print('\n!!!!!!!!!!!!median for recounting by genres!!!!!!!!!!\n')
for genre in genres.keys():
    print(genre)
    indx = top_movies_2.genres.apply(lambda x: genre in x)
    print(top_movies_2.loc[indx, ['title', 'weighted_rating_2']].head(5))
    print('\n')
