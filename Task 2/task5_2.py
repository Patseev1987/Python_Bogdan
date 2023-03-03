# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4
print("\n"*100)


def get_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif (b <0 and a > 0):
        return get_sum(a-1, b+1)
    else:
        return get_sum(a+1, b-1)    



number_1 = int(input("Enter the first numer: "))
number_2 = int(input('Enter the second number: '))
print(f"The sum {number_1} and {number_2} is {get_sum (number_1, number_2)}")
