n = int(input())

if n % 10 == 1 and n != 11:
    print(n, "korova")
elif n != 12 and n != 13 and n != 14 and (n % 10 == 4 or 2 or 3):
    print(n, "korovy")
else:
    print(n, "korov")
