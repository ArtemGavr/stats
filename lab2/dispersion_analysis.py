def read_file(filename):
    with open(filename, 'r') as reader:
        line = reader.readline()
        line.strip()  # delete spaces from front and end
        " ".join(line.split())  # get rid of duplicated spaces
        alfa = float(line)

        line = reader.readline()
        line.strip()  # delete spaces from front and end
        " ".join(line.split())  # get rid of duplicated spaces
        line_list = line.split(' ')
        p, qi = int(line_list[0]), int(line_list[1])

        matrix = [[0 for i in range(qi)] for j in range(p)]

        for i in range(p):
            line = reader.readline()
            line.strip()  # delete spaces from front and end
            " ".join(line.split())  # get rid of duplicated spaces
            line_list = line.split(' ')
            for j in range(qi):
                matrix[i][j] = float(line_list[j])

        return alfa, matrix

# matrix = [
#     [7.21, 7.55, 7.29, 7.6],
#     [7.89, 8.27, 7.39, 8.18],
#     [7.25, 7.01, 7.37, 7.53],
#     [7.75, 7.41, 7.27, 7.42],
#     [7.7, 8.28, 8.55, 8.6],
#     [7.56, 8.05, 8.07, 7.84]
# ]

# matrix = [
#     [3, 1, 2],
#     [5, 3, 4],
#     [7, 6, 5]
# ]


def count_groups_mean(matrix):
    p = len(matrix)
    qi = len(matrix[0])
    matrix_for_group_sredn = [None] * p
    # подсчет групповых средних
    for i in range(p):
        sum = 0.0
        for j in range(qi):
            sum += matrix[i][j]
        matrix_for_group_sredn[i] = (sum / qi)

    return matrix_for_group_sredn


def main():
    alfa, matrix = read_file('input.txt')
    p = len(matrix)
    qi = len(matrix[0])
    q = p * qi

    Va = p - 1
    Ve = q - p
    V = q - 1
    sum = 0.0
    for i in range(qi):
        for j in range(p):
            sum += matrix[j][i]

    average_all = sum / q

    S_zag = 0.0
    for i in range(0, p):
        for j in range(0, qi):
            S_zag += (matrix[i][j] - average_all) ** 2

    matrix_for_group_sredn = count_groups_mean(matrix)
    S_fact = 0.0  # обЪясненная сумма квадратов расстояний для explainable dispersion
    for i in range(0, p):
        S_fact += (matrix_for_group_sredn[i] - average_all) ** 2

    S_fact = qi * S_fact

    S_zal = S_zag - S_fact  # необЪясненная сумма квадратов расстояний для explainable dispersion

    MSa = S_fact / (p - 1)  # объясненная дисперсия
    MSe = S_zal / (q - p)  # необъясненная диссперсия

    F_spost = MSa / MSe

    fischer_critical_value = 2.87
    print(F_spost)
    print('H0 is', F_spost > fischer_critical_value)

main()

