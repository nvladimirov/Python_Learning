length1 = int(input())
width1 = int(input())
length2 = int(input())
width2 = int(input())

a = length1 + 1
b = length1 - 1
c = width1 + 1
d = width1 - 1
if length2 == a or length2 == b or width2 == c or width2 == d:
    print("YES")
else:
    print("NO")
