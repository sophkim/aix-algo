# 3-2. 큰 수의 법칙

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 정렬
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1 
    if m == 0:
        break
    result += second
    m -= 1

print(result)