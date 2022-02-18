import math
a = int(input("Enter a (a != 0): "))
if a == 0:
    print("Please enter again, a != 0")
else:
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    delta = b*b - 4*a*c
    if delta < 0:
        print("The equation has no solution!")
    elif delta == 0:
        x = -b / 2*a
        print("The equation has a unique solution: x = " + str(x))
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print("The equation has two differentiate solutions:\n- x1 = " + str(x1) + "\n- x2 = " + str(x2))
