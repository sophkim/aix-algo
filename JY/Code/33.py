# 33. 퇴사
# 풀이 시간: 30분

N = int(input())

time = []
price = []
dp_list = [0] * (N+1)

for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

for i in range(N):
    t = time[i]

    dp_list[i+1] = max(dp_list[i+1], dp_list[i])
    if i + t >= (N+1):
        continue
    
    dp_list[i+t] = max(dp_list[i+t], dp_list[i] + price[i])

print(dp_list)
print(max(dp_list))