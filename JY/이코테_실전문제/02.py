# 02. 곱하기 혹은 더하기
# 풀이 시간: 10분

a = str(input())
arr = []

for i in a:
    arr.append(int(i))

result = 0

for i in arr:
    if result == 0 or i == 0 or i == 1:
        result += i
    else: 
        result *= i

print(result)
        