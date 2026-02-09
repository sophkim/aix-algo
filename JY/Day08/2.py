# 실전 문제(1)
# 소요시간: 34

N, M = map(int, input().split())

parent = [0] * (N+1)

for i in range(0, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

result = []

for i in range(M):
    t, a, b = map(int, input().split())
    if t == 0: # 팀 합치기
        union(parent, a, b)
    elif t == 1: # 같은 그룹인지 확인하기
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            result.append("YES")
        else: 
            result.append("NO")
    print(parent)

for i in result:
    print(i)
        
