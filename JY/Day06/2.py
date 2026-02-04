# 실전 문제(2)
# 소요시간: -

N = int(input())

array = [0] * (N+1)
array[2] = 1
array[3] = 1

for i in range(2, len(array)):
    if i % 2 == 0:
        array[i] = min(array[i-1], array[i // 2]) + 1
    elif i % 3 == 0:
        array[i] = min(array[i-1], array[i // 3]) + 1
    elif i % 5 == 0:
        array[i] = min(array[i-1], array[i // 5]) + 1
    else:
        array[i] = array[i-1] + 1
    print(f'i:{i}, array[{i}]:{array[i]}')

print(array[N])
