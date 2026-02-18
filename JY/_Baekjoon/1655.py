# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import sys
import heapq

N = int(sys.stdin.readline())
left = [] # max heap: 작은 값들 중에서 큰 값을 출력할 것임
right = [] # min heap

for i in range(N):
    new = int(sys.stdin.readline())
    
    # 새로운 원소 삽입
    if len(left) == len(right):
        heapq.heappush(left, -new)
    else:
        heapq.heappush(right, new)

    # 원소 조정 
    if right and (- left[0]) > right[0]:
        h1 = -heapq.heappop(left)
        h2 = heapq.heappop(right)
        heapq.heappush(left, -h2)
        heapq.heappush(right, h1)

    # 중간값 출력 
    print(-left[0])