# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

print('\n'*100)


def get_find_indexs_in_range_min_max(array):
    min_array = int(input("Enter the min: "))
    max_array = int(input("Enter the max: "))
    index_array = []
    for i in range(len(array)):
        if min_array < array[i] < max_array:
            index_array.append(i)
    return index_array


my_array = [-5, 9, 0, 3, -1, -2, 1, 4, -2,
            10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

print(get_find_indexs_in_range_min_max(my_array))
