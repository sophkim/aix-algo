# 20055 컨베이어 벨트 위의 로봇

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
dur = deque(map(int, input().split()))
robots = deque([0] * N)

step = 0

while True:


    # 1. 컨베이어 벨트 회전
    dur.rotate(1)
    robots.rotate(1)
    robots[N-1] = 0 # 내리는 위치 로봇 제거

    # 2. 바로 옆 칸의 dur이 0이 아니라면 로봇들 이동
    for i in range(N-2, -1, -1):
        if robots[i] != 0 and robots[i + 1] == 0 and dur[i + 1] != 0:
            robots[i] = 0
            robots[i + 1] = 1
            dur[i + 1] -= 1
    robots[N-1] = 0 # 내리는 위치 로봇 제거

    # 3. 로봇 올리기
    if dur[0] != 0: # 내구도가 0이 아니라면 로봇 올리고 robots에 위치 저장
        robots[0] = 1
        dur[0] -= 1
    
    step += 1

    if dur.count(0) >= K:
        print(step)
        break
    
    

