print("Введите 3 числа")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a % 2 or b % 2 or c % 2:
    print("Yes")
else:
    print("No")