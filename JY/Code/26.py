# 26. 카드 정렬하기
# 풀이 시간: 14분
# 시간 초과!! -> heap 사용 필요

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()
result = 0

while len(arr) > 1:
    m1 = min(arr)
    arr.remove(m1)
    m2 = min(arr)
    arr.remove(m2)
    count = m1 + m2
    result += count
    arr.append(count)

print(result)
