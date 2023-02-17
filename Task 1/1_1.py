# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
sum = 0
number = int(input("Enter the number: "))
while number != 0:
    sum = sum+(number % 10)
    number = number//10
print("Sum is ", sum)