# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
a = [randint(0, 15)
     for i in range(int(input("Enter the size of the first set: ")))]
b = [randint(0, 15)
     for i in range(int(input("Enter the size of the second set: ")))]
print(a)
print(b)
print(f"It is new set  {sorted(list(set(a) & set(b)))}")
