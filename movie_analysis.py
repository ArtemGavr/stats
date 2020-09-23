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
import matplotlib.pyplot as plt

df = pandas.read_csv('tmdb_5000_movies.csv')
# print(df)

# # plotting all number params
dataset = pandas.DataFrame(df)
# dataset.head()
fig = plt.figure(figsize=(8, 8))
ax = fig.gca()
dataset.hist(ax=ax)
plt.show()

min_my = 10 ** 10
for i in df['vote_count']:
    if i < min_my:
        min_my = i

counter = 0
sum_my = 0
for i in df['vote_average']:
    sum_my += i
    counter += 1

av_vote = sum_my / counter

new_rating = [None] * len(df['title'])
# for n in df['title']:
# print(df['title'][0].index)
