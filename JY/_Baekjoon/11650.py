# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(f"{arr[i][0]} {arr[i][1]}")
