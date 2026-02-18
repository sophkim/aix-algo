# 최대 힙
# https://www.acmicpc.net/problem/11279

import heapq
import sys

N = int(input())
arr = []

h = []
for i in range(N):
    i = int(sys.stdin.readline())
    if i == 0 and len(h) != 0:
        print(-heapq.heappop(h))
    elif i == 0:
        print(0)
    else:
        heapq.heappush(h, -i)
