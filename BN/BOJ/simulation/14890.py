# 14890 경사로

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    # 경사로는 겹치면 안됨 그래서 visited 배열을 사용
    visited = [False] * N

    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
    
        # 오르막이면 현재 위치에서 뒤로 L칸이 같은 높이인지 검사
        if line[i] + 1 == line[i+1]: # 현재 칸보다 다음 칸이 높이가 1 높다
            for j in range(i, i-L, -1): # 현재 위치 i부터 뒤로 L칸 검사
                if j < 0 or line[j] != line[i] or visited[j]: # 범위 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면
                    return False
                visited[j] = True

        # 내리막
        elif line[i] - 1 == line[i+1]:
            for j in range(i+1, i+L+1):
                if j >= N or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True
        
        else:
            return False

    return True

count = 0

# 행 검사
for i in range(N):
    if check(graph[i]):
        count += 1

# 열 검사
for j in range(N):
    col = [graph[i][j] for i in range(N)] # j번째 열을 하나의 리스트로 만든다
    if check(col):
        count += 1


print(count)