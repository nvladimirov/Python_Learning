def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')


print_max(3, 4)  # прямая передача значений
x = 5
y = 7
print_max(x, y)  # передача переменных в качестве аргументов
