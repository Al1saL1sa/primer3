print("Ведите число: ")
j = 0
n = int(input())
print('   ', end=' ')
for i in range(1, n):
    print(' ', i, end=' ')
print(' ', sep = ' ')
i = 0
for i in range(1, n + 1):
    for j in range(i, n + i):
        print(' ', j, end = ' ')
    print(' ', sep = ' ')
    j = 0