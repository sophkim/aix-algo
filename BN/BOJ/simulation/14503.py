# 14503 로봇 청소기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

map_info = []
for i in range(N):
    map_info.append(list(map(int, input().split())))


# 방문 기록 맵 생성
d = [[0] * M for _ in range(N)]

# 청소 시작 위치
d[x][y] = 1

# 북동남서 순으로 방향 이동 정의 (수학 좌표계랑 다름!)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계 방향 90도 회전 함수
def turn_left(direction):
    # 0 북, 1 동, 2 남, 3 서
    return (direction - 1) % 4

# 시뮬레이션 시작
count = 1 # 청소한 칸
turn_time = 0 # 회전 횟수
while True:
    direction = turn_left(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 이동 가능하면 이동
    if d[nx][ny] == 0 and map_info[nx][ny] == 0: # 방문 안했고 & 청소 no 상태라면
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    else: # 이동 못하면 회전 카운트 증가
        turn_time += 1

    if turn_time == 4: # 사방이 막혔다면
        # 방향유지하고 한 칸 후진
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map_info[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
