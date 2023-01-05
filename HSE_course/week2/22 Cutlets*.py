k = int(input())
m = int(input())
n = int(input())

if k < n and n % k == 0:
    print(m * 2 * (n // k))
elif k < n and n % k > 0:
    print(m * 2 * (n // k + 1))
elif k >= n:
    print(m * 2)
