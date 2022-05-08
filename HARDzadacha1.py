import math
EPS = 1e-10

x = float(input("Value of x = "))
if x < 0 or 2 < x:
    print("Enter numbers between 0 and 2")
    exit(0)

a = -x + 1
S, k = a, 1


while math.fabs(a) > EPS:
    a *= ((-x + 1) * (k ** 2)) / ((k + 1) ** 2)
    S += a
    k += 1

print(f"{S}")