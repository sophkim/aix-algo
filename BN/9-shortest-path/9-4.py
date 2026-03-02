# 미래 도시

INF = int(1e9)

n, m = map(int, input().split())
# 2차원 리스트를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 즉, 입력으로 받는 값은 서로 연결된 것

# 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력받기
x, k = map(int, input().split())

# '점화식'에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): # 모든 (a → b)에 대해 모든 k를 중간에 넣어보는 것
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

            
# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
else:
    print(distance)