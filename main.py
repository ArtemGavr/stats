# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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
    mappa = dict.fromkeys(array, 0)
    for i in array:
        mappa[i] += 1

    max_of_usages = -1
    moda_set = []
    for k, v in mappa.items():
        if v > max_of_usages:
            max_of_usages = v
            moda_set = [k]
        elif v == max_of_usages:
            moda_set.append(k)

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


if __name__ == '__main__':
    my_set = [1, 2, 2, 3, 4, 5, 6, 7]
    print(f"{medium_value(my_set)} - medium value")
    # print(f"{dispersion(my_set)} - dispersion")  # TODO incorrect
    # TODO стандартне выдхидення
    print(f"{median(my_set)} - median")
    print(f"{moda(my_set)} - moda/ modas")
    print(f"{max_min(my_set)} - max/ min")

    m_m = max_min(my_set)
    print(f"{m_m[0] - m_m[1]} - rozmax")
    print_hi("elina")
    # TODO quantile
