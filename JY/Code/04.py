# 04. 만들 수 없는 금액
# 풀이 시간: -분

N = int(input())
coins = list(map(int, input().split()))

target = 1
coins.sort()

for i in coins:
    if target >= i:
        target += i
    else:
        break

print(target)



