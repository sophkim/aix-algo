# 24. 안테나
# 풀이 시간: 6분

N = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = 1e9
index = -1

for i in range(min(arr), max(arr)+1):
    antenna = 0
    for j in arr:
        antenna += abs(j-i)
    if antenna < result:
        result = antenna
        index = i

print(index)
    


