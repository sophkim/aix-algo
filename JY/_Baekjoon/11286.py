# 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq

N = int(sys.stdin.readline())

h = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0 and h:
        print(heapq.heappop(h)[1])
    elif num == 0:
        print(0)
    else:
        heapq.heappush(h, (abs(num), num))
    