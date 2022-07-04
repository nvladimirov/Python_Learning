N = int(input())

h = N // 3600
m1 = N // 600 % 6
m2 = N // 60 % 10
s = N % 60
s1 = N // 60 % 6
s2 = s % 10
print(h, ":", m1, m2, ":", s1, s2, sep="")
