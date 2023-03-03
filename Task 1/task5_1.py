# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
print("\n"*100)


def get_exponentiate(a, b):
    if b == 0:
        return 1
    return a*get_exponentiate(a, b-1)


n = int(input("Enter the number: "))
m = int(input("Enter the number for exponentiate: "))
print(get_exponentiate(n, m))
