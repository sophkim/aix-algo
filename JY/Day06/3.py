# 실전 문제(3)
# 소요시간: 8분


N = int(input())

shed = list(map(int, input().split()))

result = [0] * N 
result[0] = shed[0]
result[1] = max(shed[0], shed[1])

for i in range(2, N):
    result[i] = max(result[i-1], result[i-2]+shed[i])

print(result)
print(result[N-1])