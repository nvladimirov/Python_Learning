a = int(input())
b = int(input())
c = int(input())

n = a % 2
m = b % 2
g = c % 2

if (n == 0 or m == 0 or g == 0) and (n != 0 or m != 0 or g != 0):
    print("YES")
else:
    print("NO")
