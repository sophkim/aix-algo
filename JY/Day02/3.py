# 실전 문제(1)
# 소요시간: 13분 

# 영어 대문자 아스키 코드 시작: 65
# 영어 소문자 아스키 코드 시작: 97

pos = input()
x = int(pos[1])
y = int(ord(pos[0]) - 96)

move = [[-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2], [2, 1], [2, -1]]

result = 0

for mv in move:
    nx = x + mv[0]
    ny = y + mv[1]

    if 0 < nx < 9 and 0 < ny < 9:
        result += 1
    
print(result)
        