# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


sum = 0
sum_1 = 0
flag = True
while flag:
    ticket_number = int(input("Enter th six-difit ticket number: "))
    if ticket_number > 99999 and ticket_number < 1000000:
        flag = False
        while ticket_number > 0:
            if ticket_number > 0 and ticket_number < 1000:
                sum = sum + ticket_number % 10
                ticket_number = ticket_number//10
            else:
                sum_1 = sum_1+ticket_number % 10
                ticket_number = ticket_number//10
        if sum == sum_1:
            print("This ticket number is lucky!")
        else:
            print("This ticket number is not lucky!")
    else:
        print("You entered wrong number! Try again!")
