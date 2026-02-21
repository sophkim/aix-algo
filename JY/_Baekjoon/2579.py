# 계단 오르기
# https://www.acmicpc.net/problem/2579

N = int(input()) # 계단 개수

stair = [0] # 총 (N+1) 개

for _ in range((N)):
    stair.append(int(input()))

result = [0]*max((N+1),4)

result[1] = stair[1]
if N > 1:
    result[2] = stair[1]+stair[2]
if N > 2:
    result[3] = max(stair[1]+stair[3], stair[2]+stair[3])

for i in range(4, N+1):
    result[i] = max(result[i-2]+stair[i], result[i-3]+stair[i-1]+stair[i])

print(result[N])