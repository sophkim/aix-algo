# 최소 힙
# https://www.acmicpc.net/problem/1927


import sys
import heapq

N = int(sys.stdin.readline())
h = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0 and h:
        print(heapq.heappop(h))
    elif n == 0:
        print(0)
    else:
        heapq.heappush(h, n)
