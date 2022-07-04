n = int(input())
# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
k = 1
if n == 1:
    print("YES")
while k != n:
    if n % 2 != 0:
        print("NO")
        break
    k = k * 2
    if n == k:
        print("YES")
        break
    else:
        print("NO")
        break
