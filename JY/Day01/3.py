# 풀이 시간: 4분

N, M = map(int, input().split())

card = []
for _ in range(N):
    card.append(min(list(map(int, input().split()))))

print(max(card))


