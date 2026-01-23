# 3-3. 숫자 카드 게임

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


result = []

for row in arr:
    min_val = min(row)
    result.append(min_val)
    min_idx = row.index(min_val)
    #print(min_idx, min_val)
    
print(max(result))