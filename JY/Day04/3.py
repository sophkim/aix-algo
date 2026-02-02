# 실전 문제(2)
# 소요시간: 4분 

n = int(input())

array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, score))

array.sort(key = lambda data: data[1])

for i in range(n):
    print(array[i][0], end=" ")