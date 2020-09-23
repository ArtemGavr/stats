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
import matplotlib.pyplot as plt

df = pandas.read_csv('tmdb_5000_movies.csv')

# # plotting all number params
# dataset = pandas.DataFrame(df)
# fig = plt.figure(figsize=(8, 8))
# ax = fig.gca()
# dataset.hist(ax=ax)
# plt.show()

min_my = 10 ** 10
for i in df['vote_count']:
    if i < min_my:
        min_my = i

counter = 0
sum_my = 0
for i in df['vote_average']:
    sum_my += i
    counter += 1

c = sum_my / counter # aver vote count
new_rating = [0] * len(df['title'])
mappa = [df['title'].to_list(), new_rating]
for n in df['title']:
    ser = df['title'].to_list()
    index = ser.index(n)
    r = df['vote_average'][index]
    v = df['vote_count'][index]
    if v == 0 and min_my == 0:
        mappa[1][index] = 0
    else:
        mappa[1][index] = (v * r / (v + min_my)) + (min_my * c / (v + min_my))

top10_ratings = [(-1, -1)]*10 # index value

for n in range(0, len(mappa[1])):
    for i in range(0, len(top10_ratings)):
        if mappa[1][n] > top10_ratings[i][1]:
            top10_ratings[i] = (n, mappa[1][n]) # index:value pair
            break

top10_films = []
for i in top10_ratings:
    name = mappa[0][i[0]]
    top10_films.append((name, i[1]))

print('Top 10 movies: ', top10_films)
