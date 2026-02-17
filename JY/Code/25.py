# 25. 실패율

def solution(N, stages):
    # 실패율: (도달o & 클리어x) 플레이어 수 / 도달o 플레이어 수
    arr = []
    result = []

    stages.sort()
    length = len(stages)

    for i in range(1, N+1):
        if i not in stages:
            arr.append((0,i))
        else:
            idx = stages.index(i)
            failure = stages.count(i) / (length - idx)
            arr.append((failure,i))

    arr.sort(key = lambda x: (-x[0], x[1]))

    for i in arr:
        result.append(i[1])

    return result

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))