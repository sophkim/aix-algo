# 효율적인 화폐 구성

# 그리디 거스름돈 문제와 동일하나, 화폐 단위에서 큰 단위가 작은 단위의 배수는 아니기에 그리디로 풀기가 불가능

n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001] * (m + 1)

# dp 바텀업
d[0] = 0 # 0원을 만드는 데 필요한 화폐 개수는 0개
for i in range(n): # for 각 동전
    for j in range(array[i], m + 1): # for 그 동전으로 만들 수 있는 금액들
        d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])