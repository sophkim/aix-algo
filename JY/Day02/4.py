# 실전 문제(2)
# 소요시간: 1시간 이상 (2번의 시도)
# 이유: 문제 조건을 잘못 해석함 (방문한 칸 수를 이동 횟수로 해석함)

N, M = map(int, input().split())

x, y, d = map(int, input().split())

game_map = []

for _ in range(N):
    game_map.append(list(map(int, input().split())))

game_map[x][y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mv = 1

while True:
    find = [] # 첫번째 원소: 왼쪽 방향 칸 정보
    for i in range(4):
        d = (d+3) % 4 # 왼쪽 회전
        nx = x + dx[d]
        ny = y + dy[d]
        find.append(game_map[nx][ny])


    if find[0] == 0: # 왼쪽이 육지(0)면 -> 회전과 이동
        d = (d+3) % 4
        x = x + dx[d]
        y = y + dy[d] 
        game_map[x][y] = 2
        mv += 1
    
    elif 0 in find: # 이동할 수 있는 타일이 존재하면 -> 회전만
        d = (d+3) % 4
    
    else: # 바다 혹은 이미 이동했던 타일만 존재하면 -> 뒤로 이동
        dn = (d+2) % 4
        x = x + dx[dn]
        y = y + dy[dn] 
        if game_map[x][y] == 1: # 뒤로 이동한 타일이 바다면
            break

print(mv)