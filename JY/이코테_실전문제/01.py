# 01. 모험가 길드
# 풀이 시간: 20분

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

count = 0
result = 0

for i in range(N):
    count += 1
    if arr[i] == count:
        result += 1
        count = 0

print(result)