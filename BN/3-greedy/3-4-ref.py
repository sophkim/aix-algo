# 3-3. 1이 될 때까지

n, k = map(int, input().split())

result = 0

while True:
    # N == K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target) # target이 될 때까지 1씩 빼야 하는 횟수를 한 번에 더함
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    
    # K로 나누기
    result += 1
    n //= k

result += (n - 1) # 루프 종료 후 남은 N을 1로 만들기 위한 -1 연산 횟수
print(result)