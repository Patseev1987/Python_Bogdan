# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

number_rows = int(input("Enter the number of rows chokolade: "))
number_columns = int(input("Enter the number of columns chokolade: "))

number_of_part = int(
    input("Enter the number of chokolade what you want to take: "))

if (number_of_part % number_rows == 0 or number_of_part % number_columns == 0) and number_rows*number_columns > number_of_part:
    print("Yes! You can take this piece.")
else:
    print("No!  You can not take this piece.")
