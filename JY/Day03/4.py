# 실전 문제(1)
# 소요시간: 28분

from collections import deque

N, M = map(int, input().split())

graph = [] # 전체 맵 정보 
visited = [[False]*M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: 
            visited[i][j] = True


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

def bfs(start, visited):
    queue = deque()
    x, y = start
    visited[x][y] = True
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny <M and not visited[nx][ny]: 
                visited[nx][ny] = True
                queue.append((nx,ny))

    global count
    count += 1

for i in range(N):
    for j in range(M):
        if not visited[i][j]: 
            bfs((i,j), visited)


print(count)