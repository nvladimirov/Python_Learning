n = int(input())

# Дано натуральное число n.
# Напечатайте все n-значные нечетные натуральные числа в порядке убывания
b = n % 2
if b == 0:
    for i in range(n - 1, 0, -2):
        print(i, end=' ')
else:
    for i in range(n, 0, -2):
        print(i, end=' ')
