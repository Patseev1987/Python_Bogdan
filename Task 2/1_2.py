# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

number =int(input("Enter the number of cranes: "))
x= None
if number%6==0:
  x=number//6
  print("Petr made ", x)
  print("Sergey made ", x)
  print("Kate made ", (x+x)*2)
else:
  print("No solution!")