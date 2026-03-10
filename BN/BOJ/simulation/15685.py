# 15685 드래곤 커브

import sys

input = sys.stdin.readline

# 드래곤 커브의 개수 입력받기
N = int(input())

# 방문 기록 맵 초기화
d = [[0] * 101 for _ in range(101)]

# 90도 회전 함수
def turn_left(direction):
    return (direction + 1) % 4

# 방향 이동 정의 (0,1,2,3 순)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


# 드래곤 커브 생성
for _ in range(N):
    x, y, direction, generation = map(int, input().split())

    dirs = [direction] # 하나의 드래곤 커브에 대해 최종 방향을 저장하는 리스트

    # 핵심 드래곤 커브 규칙: 기존 방향을 뒤집는다 > 90도 회전 > 뒤에 붙인다
    # 즉 끝점을 기준으로 회준하는 것은 기존 방향 리스트를 뒤집고 각 방향을 +1 한 것임
    for _ in range(generation): 
        for k in reversed(dirs):
            dirs.append((k + 1) % 4)

    d[x][y] = 1
    # print("dirs: ", dirs)

    for dir in dirs:
        x += dx[dir]
        y += dy[dir]
        d[x][y] = 1

ans = 0

for i in range(100):
    for j in range(100):
        if d[i][j] and d[i+1][j] and d[i][j+1] and d[i+1][j+1]:
            ans += 1

print(ans)