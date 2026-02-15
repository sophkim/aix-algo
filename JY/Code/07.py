# 07. 럭키 스트레이트
# 풀이 시간: 4분

data = input()

length = len(data)

left = 0
right = 0

for i in range(0, length//2):
    left += int(data[i])

for i in range(length//2, length):
    right += int(data[i])

if left == right:
    print("LUCKY")
else:
    print("READY")