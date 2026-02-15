# 15. 특정 거리의 도시 찾기
# 풀이 시간: 7분

from collections import deque

N, M, K, X = map(int, input().split()) # 노드, 간선, 최단 거리, 시작 노드

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # a에서 b로 이동 가능 

visited = [False] * (N+1)

INF = 1e9
cost = [1e9] * (N+1)

queue = deque()
queue.append(X)
visited[X] = True
cost[X] = 0

while queue:
    v = queue.popleft()
    
    for i in graph[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            cost[i] = cost[v] + 1

if K not in cost:
    print(-1) 

for i in range(1, N+1):
    if cost[i] == K:
        print(i)
    

