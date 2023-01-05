A = int(input())
B = int(input())
N = int(input())

costR = (N * (A * 100 + B)) // 100
costK = (N * (A * 100 + B)) % 100

print(costR, costK)
