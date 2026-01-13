# 풀이 시간: 19분

N, M, K = map(int, input().split())

data = list(map(int,input().split()))

data.sort(reverse=True)

a = data[0]
b = data[1]

result = 0

result += (M//(K+1)) * (K*a + b)
result += (M%(K+1)) * a

print(result)


# 예시 답안(1)
'''
n, m, k = map(int, input().split())

data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    else:
        result += second
        m -= 1

print(result)
'''


# 예시 답안(2)
'''
n, m, k = map(int, input().split())

data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

print(result)
'''