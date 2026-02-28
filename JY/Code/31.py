# 31. 금광
# 풀이 시간: 38분

for tc in range(int(input())):

    n, m = map(int, input().split())

    gold = list(map(int, input().split()))
    dp_list = [0] * (n*m)

    # 첫번째 열 dp 리스트 초기화
    for i in range(n):
        dp_list[i*m] = gold[i*m]

    for col in range(0, m-1):
        for row in range(0, n):
            idx = (row*m) + col
            dp_list[idx+1] = max(dp_list[idx+1], dp_list[idx] + gold[idx+1])
            if idx >= m:
                dp_list[idx+1-m] = max(dp_list[idx+1-m], dp_list[idx] + gold[idx+1-m])
            if idx < 2*m:
                dp_list[idx+1+m] = max(dp_list[idx+1+m], dp_list[idx] + gold[idx+1+m])

    result = 0
    for row in range(1, n+1):
        result = max(result, dp_list[row*m-1])

    print(result)

