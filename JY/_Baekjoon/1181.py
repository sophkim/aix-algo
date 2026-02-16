# 단어 정렬

N = int(input())

arr = []
for _ in range(N):
    arr.append(input())


arr.sort(key = lambda x: (len(x), x)) 

result = [arr[0]]

for i in range(0, N-1):
    if arr[i] != arr[i+1]:
        result.append(arr[i+1])

for k in result:
    print(k)