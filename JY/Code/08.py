# 08. 문자열 재정렬
# 풀이 시간: 7분
# 수정 사항: [코너 케이스] 문자열에 숫자가 없는 경우를 고려해야 함

arr = list(input())

string = []
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

count = 0
flag = 0

for i in arr:
    if i in number:
        count += int(i)
    else:
        string.append(i)

string.sort()
for i in string:
    print(i, end="")
if count != 0:
    print(count)