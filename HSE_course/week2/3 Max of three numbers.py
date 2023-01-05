x = int(input())
y = int(input())
z = int(input())

if x > y > z or x > y == z:
    print(x)
elif x < y > z or y > x == z:
    print(y)
elif x < y < z or z > x == y:
    print(z)
else:
    print("все равны")
