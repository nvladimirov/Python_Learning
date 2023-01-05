N = int(input())

n = 1
k = n
while k <= N:
    print(n ** 2, end=' ')
    k = (n + 1)**2
    n = (n + 1)
