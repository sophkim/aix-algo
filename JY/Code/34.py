# 34. 병사 배치하기
# 풀이 시간: -
'''
해결 방법: 최장 증가 부분 수열

dp[i]
- 0 ~ i-1번째 원소에 대하여 i번째 원소보다 작은 수 중에 가장 큰 수를 확인.
- 가장 큰 수의 dp값 + 1
'''

N = int(input())

dp_list = [1] * N

soldier = list(map(int, input().split()))

soldier.reverse()

for i in range(N):
    for j in range(0, i):
        if soldier[i] > soldier[j]:
            dp_list[i] = max(dp_list[i], dp_list[j]+1)

print(N - max(dp_list))