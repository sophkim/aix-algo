# DFS 구현 예제

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 방문하지 않은 노드라면?
            dfs(graph, i, visited) # 방문하고 스택에 추가

dfs(graph, 1, visited)