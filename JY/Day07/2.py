# 실전 문제(2)
# 소요시간: 26분
# 양방향 그래프 노드 관리하는 법 숙지


import heapq

INF = int(1e9)

n, m = map(int, input().split()) # 노드, 간선

graph = [[] for _ in range(n+1)]

distance_K = [INF] * (n+1)
distance_X = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(1, distance_K)
dijkstra(K, distance_X)

if distance_K[K] == INF or distance_X[X] == INF:
    print(-1)
else:
    print(distance_K[K] + distance_X[X])