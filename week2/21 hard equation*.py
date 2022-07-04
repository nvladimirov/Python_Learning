a = int(input())
b = int(input())
c = int(input())
d = int(input())

D = (b * c + d * a) ** 2 - 4 * a * c * b * d
print(D)
if a * c == b * d == 0:
    print("INF")
elif D > 0:
    x1 = (-(b * c + d * a) + D ** 0.5) / (2 * c * a)
    x2 = (-(b * c + d * a) - D ** 0.5) / (2 * c * a)
    print(x1, x2)
elif D == 0:
    x = (-(b * c + d * a)) / (2 * c * a)
    print(x)
else:
    print("NO")
не работает