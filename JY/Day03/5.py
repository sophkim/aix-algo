# 실전 문제(2)
# 소요시간: 30분 

from collections import deque

N, M = map(int, input().split())

graph = []
visited = [[False]*M for _ in range(N)]
distance = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            visited[i][j] = True

queue = deque()

def bfs(x, y, visited):
    visited[x][y] = True
    queue.append((x, y))

    while not visited[N-1][M-1]:
        x, y= queue.popleft()
        d = distance[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = d + 1
                queue.append((nx, ny))


bfs(0, 0, visited)

print()
print(distance[N-1][M-1] + 1)

print()
for i in range(N):
    print(distance[i])
