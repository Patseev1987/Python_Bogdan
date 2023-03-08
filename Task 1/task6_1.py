# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

print('\n'*100)


def get_fill_progression():
    result = []
    first = int(
        input("Enter the first element in progression (a(n) = a1 + (n - 1)*d): "))
    d = int(input("Enter the d in progression (a(n) = a1 + (n - 1)*d): "))
    size = int(
        input("Enter the number of progression elements (a(n) = a1 + (n - 1)*d): "))
    for i in range(size):
        result.append(first+((i+1)-1)*d)
    return result


def print_progression(progression):
    for i in range(len(progression)):
        print(f"This is {i+1} elemnt in progression --->  {progression[i]}")


my_progression = get_fill_progression()
print_progression(my_progression)
