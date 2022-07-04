H = int(input())
A = int(input())
B = int(input())

day_way = A - B
way = (H - A - 1) // day_way + 1 + 1
print(way)
