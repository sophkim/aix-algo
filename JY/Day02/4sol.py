# 실전 문제(2)
# 모범 답안

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 map 

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))\
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): # 반시계 방향 회전 함수를 따로 작성
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1 
turn_time = 0 # 방향 전환 횟수를 카운팅하며 코드 작성
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] ==0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction] # 뒤로 이동할 때, 방향을 고정하고 위치만 바꿔주는 방법
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)