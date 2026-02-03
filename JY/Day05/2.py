# 실전 문제(1)
# 소요시간: 4분

N = int(input())
store = list(map(int, input().split()))

M = int(input())
consumer = list(map(int, input().split()))

for i in range(M):
    if consumer[i] in store:
        print("yes", end=" ")
    else:
        print("no", end=" ")