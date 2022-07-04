a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or c + b <= a:
    print("impossible")
elif a**2 + b**2 == c**2:
    print("rectangular")
elif a**2 + c**2 == b**2:
    print("rectangular")
elif c**2 + b**2 == a**2:
    print("rectangular")
elif a ** 2 + b ** 2 < c ** 2:
    print("acute")
elif a ** 2 + b ** 2 > c ** 2:
    print("obtuse")
