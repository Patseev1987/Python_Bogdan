print("\n"*100)

s = int(input("Enter the sum of numbers: "))
p = int(input("Enter the product of numbers: "))
if p == 0 and s >= 0:
    print(f"Numbers are {s} and {p}.")
elif s**2-4*p >= 0:
    for x in range(1, p+2):
        if s == x+(p/x) and p == x*(s-x):
            print(f"The first number is {x} and second number is {s-x}")
            break
else:
    print("There is not solution!")
