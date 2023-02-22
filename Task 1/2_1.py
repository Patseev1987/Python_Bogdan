# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random
print("\n"*100)

number = int(input("Enter the number of coin: "))
coin_sight = None
count = 0

for coin in range(number):
    coin_sight = random.randint(0, 1)
    if coin_sight == 1:
        count += 1
        print("Eagl")
    else:
        print("Tails")
if count >= number/2:
    print(f"You should turn {number-count} coins.")
else:
    print(f"You should turn {count} coins.")
