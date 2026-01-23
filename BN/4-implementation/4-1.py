# chaper 4 구현은 완전 탐색과 시뮬레이션을 합친 파트
# 완전 탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

# 4-1. 상하좌우
n = int(input())
data = input().split()

x = 1
y = 1

for i in data:
    if i == "L" and y > 1:
        y -= 1
        #print("L: ", x, y)
    elif i == "R" and y < n:
        y += 1
        #print("R: ", x, y)
    elif i == "U" and x > 1:
        x -= 1
        #print("U: ", x, y)
    elif i == "D" and x < n:
        x += 1
        #print("D: ", x, y)
    else:
        print("None")

print(x, y)