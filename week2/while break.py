now = int(input())

maxNum = now
while now != 0:
    now = int(input())  # начинаем цикл со ввода числа
    if now == 0:
        break  # прекращаем цикл как только ввели ноль. Break отвечает за прерывание цикла
    if now > maxNum:  # либо вместо break можно написать логическиое "and now != 0"
        maxNum = now
print(maxNum)
