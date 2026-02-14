# 03. 문자열 뒤집기
# 풀이 시간: 24분

num = input()

result = [0, 0]

flag = int(num[0])
result[flag] +=1

for i in num:
    i = int(i)
    if i != flag:
        result[i] += 1
        flag = i


print(min(result))