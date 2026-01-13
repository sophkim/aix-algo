# heapq 라이브러리

# 우선순위 큐 기능 규현에 사용
# 최소 힙으로 구성 -> 오름차순 정렬 O(NlogN) 
# heapq.heappush(): 원소 삽입
# heapq.heappop(): 원소 추출

import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h,value)
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


def heapsort_rev(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result

result = heapsort_rev([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)