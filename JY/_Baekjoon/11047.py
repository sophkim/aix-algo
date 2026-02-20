# 동전 0
# https://www.acmicpc.net/problem/11047

import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

result = 0

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        cnt = K // coins[i]      
        result += cnt
        K -= cnt * coins[i]      

print(result)