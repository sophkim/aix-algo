# 시리얼 번호

N = int(input())

serial = []

for _ in range(N):
    text = input()
    serial.append([len(text), text])

for i in range(N):
    count = 0
    for j in serial[i][1]:
        if str(j).isdigit():
            count += int(j)
    serial[i].append(count)        


serial.sort(key = lambda x: (x[0], x[2], x[1]))


for s in serial:
    print(s[1])

