# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

print("\n"*100)

s = int(input("Enter the sum of numbers: "))
p = int(input("Enter the product of numbers: "))
f = False
if s**2-4*p >= 0:
    for x in range(1001):
        if f:
            break
        for y in range(1001):
            if f:
                break
            if s == x+y and p == x*y:
                print(f"The first number is {x} and second number is {y}")
                f = True

else:
    print("There is not solution!")
