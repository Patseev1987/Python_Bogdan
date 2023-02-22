# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

print("\n"*100)

number = int(input("Enter the number: "))
count = 2
while count <= number:
    print(count)
    count *= 2