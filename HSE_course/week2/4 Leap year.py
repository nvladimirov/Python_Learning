year = int(input())

isZ = year % 100 == 0
isX = year % 4 == 0
isY = year % 400 == 0

if isY == True and isZ == False and isX == True:
    print("YES")
elif isY == False and isZ == False and isX == True:
    print("YES")
elif isY == True and isZ == True and isX == True:
    print("YES")
elif isY == False and isZ == True and isX == True:
    print("NO")
elif isY == False and isZ == True and isX == False:
    print("NO")
else:
    print("NO1")
