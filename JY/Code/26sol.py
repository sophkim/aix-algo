# Heap

import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    m1 = heapq.heappop(heap)
    m2 = heapq.heappop(heap)
    sum_value = m1 + m2
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)