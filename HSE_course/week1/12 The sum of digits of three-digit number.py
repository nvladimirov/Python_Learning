N = int(input())
first = N // 100
second = (N // 10) % 10
third = N % 10

print(first + second + third)
