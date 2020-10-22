# from lab1 import main as stats

alfa = 0.05
p, qi = 6, 4
q = p * qi

Va = p - 1
Ve = q - p
V = q - 1

matrix = [[None] * qi] * (p + 1)
# with open('dog_breeds.txt', 'r') as reader:
#     line = reader.readline()
#
#    for line in reader.readlines():
#       print(line, end='')
matrix = [
    [7.21, 7.55, 7.29, 7.6],
    [7.89, 8.27, 7.39, 8.18],
    [7.25, 7.01, 7.37, 7.53],
    [7.75, 7.41, 7.27, 7.42],
    [7.7, 8.28, 8.55, 8.6],
    [7.56, 8.05, 8.07, 7.84],
    [None] * qi
]

for i in range(0, qi):
    sum = 0.0
    for j in range(0, p):
        sum += matrix[j][i]
    matrix[p][i] = (sum / p)

sum = 0.0
for i in range(0, qi):
    for j in range(0, p):
        sum += matrix[j][i]

average_all = sum / q

S_all = 0.0
for i in range(0, p):
    for j in range(0, qi):
        S_all += (matrix[i][j] - average_all) ** 2

S_fact = 0.0
for i in range(0, qi):
        S_fact += (matrix[p][i] - average_all) ** 2

S_fact *= q

print(S_fact)
