n = int(input())  # По данному натуральному числу N
# выведите такое наименьшее целое число k, что 2ᵏ≥N.
# У меня в решении 2ᵏ - это p

k = 0
p = 1
while p < n:
    p = p * 2
    k = k + 1
print(k)
