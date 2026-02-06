# 실전 문제(3)
# 소요시간: 14분 

import heapq
INF = int(1e9)

N, M, C = map(int, input().split()) # 노드, 간선, 시작점

distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(C)
print(distance)

count = 0
max_dist = 0
for i in range(1, N+1):
    if distance[i] == INF:
        continue
    else:
        if max_dist < distance[i]:
            max_dist = distance[i]
        count += 1

print(count - 1, max_dist)