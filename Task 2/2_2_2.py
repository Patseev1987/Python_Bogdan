print("\n"*100)
s = int(input("Enter the sum of numbers: "))
p = int(input("Enter the product of numbers: "))
d = ((-s)**2)-4*p
x = None
y = None
if d >= 0:
    x = (-(-s)+d**(1/2))/2
    y = (-(-s)-d**(1/2))/2

    print(f"The first number is {int(x)} and second number is {int(y)}")
else:
    print("There is not solution!")
