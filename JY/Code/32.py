# 32. 정수 삼각형
# 풀이 시간: 30분

n = int(input())
tri = []
dp_list = []

for i in range(n):
    tri.append(list(map(int, input().split())))
    dp_list = [row[:] for row in tri]

for i in range(0, n-1):
    for j in range(0, i+1):
        dp_list[i+1][j] = max(dp_list[i+1][j], dp_list[i][j] + tri[i+1][j])
        dp_list[i+1][j+1] = max(dp_list[i+1][j+1], dp_list[i][j] + tri[i+1][j+1])


result = 0
for i in range(n):
    result = max(result, dp_list[n-1][i])

print(result)