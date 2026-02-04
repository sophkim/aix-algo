# 실전 문제(4)
# 소요시간: 9분

N = int(input())

result = [0] * (N+1) # 0 ~ N 까지 (1 ~ N 사용)

result[1] = 1
result[2] = 3

for i in range(3, N+1):
    result[i] = result[i-1] + (result[i-2] * 2)

print(result)
print(result[N] % 796796)