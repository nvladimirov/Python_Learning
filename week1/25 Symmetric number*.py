N = int(input())
N1 = N // 1000
N2 = N // 100 % 10
N3 = N // 10 - N1 * 100 - N2 * 10
N4 = N % 10
print((N1 - N4) ** 2 + (N2 - N3) ** 2 + 1)
