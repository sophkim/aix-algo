# 실전 문제(5)
# 소요시간: 약 1시간

N, M = map(int, input().split())

dp_list = [0] * 20000 # (1 ~ 10000) 사용

coin = []

for i in range(N):
    c = int(input())
    coin.append(c)
    dp_list[c] = 1

coin.sort()
s = coin[0]

for i in range(s, M+1):
    if dp_list[i] == 0:
        continue
    
    for j in coin:
        if dp_list[i+j] == 0:
            dp_list[i+j] = dp_list[i] + 1
        else:
            dp_list[i+j] = min(dp_list[i] + 1, dp_list[i+j])

if dp_list[M] == 0:
    print(-1)
else:
    print(dp_list[M])