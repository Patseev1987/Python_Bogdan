# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

print("\n"*100)

number = int(input("Enter the number: "))
my_list = [i for i in range(1, number+1)]
print(my_list)
number_search = int(input("Enter the number to search: "))
counter = my_list.count(number_search)
print(counter)
