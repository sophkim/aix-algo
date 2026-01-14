# 예제 문제(2)
# 소요시간: 6분

N = int(input())

result = 0

for i in range(0, N+1):
    for j in range(0, 60):
        for k in range(0,60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                result += 1

print(result)