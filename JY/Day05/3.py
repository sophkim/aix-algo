# 실전 문제(2)
# 소요시간: 33분 
# 정답은 맞으나... 떡의 길이(M)를 늘릴 때마다 이진 탐색을 통하여 적절한 인덱스를 찾기 때문에 최적의 코드는 아님. 

N, M = map(int, input().split())
cake = list(map(int, input().split()))
cake.sort()

max_h = max(cake)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

result = 0
for i in range(1, max_h):
    index = binary_search(cake, i, 0, N-1)
    sum_all = sum(cake[index:]) 
    if (sum_all - (N-index)*i) >= M:
        result += 1
    else:
        break

print(result)