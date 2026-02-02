# 실전 문제(3)
# 소요시간: 6분

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

result = 0

for i in range(k):
    if A[i] < B[i]:
        result += B[i]
    else:
        result += A[i]

for i in range(k, n):
    result += A[i]

print(result)
