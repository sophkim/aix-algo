# 15662 톱니바퀴(2)

import sys
from collections import deque

input = sys.stdin.readline

# n = 0 , s = 1
# 1 = 시계 , -1= 반시계

T = int(input()) # 톱니바퀴의 개수
gears = [deque(map(int, input().strip())) for _ in range(T)]

K = int(input()) # 회전횟수
turn = [list(map(int, input().split())) for _ in range(K)]

def solution(T, gears, K, turn):

    for target, direction in turn:
        
        rotate_list = []

        # target 기어 우측 확인
        for i in range(target, T):
            if gears[i][6] != gears[i - 1][2]:
                rotate_list.append(i) # 회전해야할 기어 index 저장
            else:
                break
        
        # target 기어 좌측 확인
        for i in range(target - 2, -1, -1):
            if gears[i][2] != gears[i + 1][6]:
                rotate_list.append(i)
            else:
                break

        # target 기어 회전
        gears[target - 1].rotate(direction)

        # t 기어와 맞닿은 극이 다른 기어 회전
        for element in rotate_list:
            gears[element].rotate(-direction if (element - (target-1)) % 2 else direction) # target에서 몇 칸 떨어졌나? 홀수면 - 짝수면 +
    
    return sum(gear[0] for gear in gears)

        

result = solution(T, gears, K, turn)
print(result)

