# 최고의 33위치

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = 0
for i in range(0, n-2):
    for j in range(0, n-2):
        coin = 0
        for x in range(0,3):
            for y in range(0,3):
                coin += grid[x+i][j+y]
        result = max(result, coin)

print(result)