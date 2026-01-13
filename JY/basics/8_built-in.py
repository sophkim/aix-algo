# 기본 내장 라이브러리 표준 함수

# sum: iterable 객체를 입력으로 받아 모든 원소의 합 반환
print(sum([1,2,3]))

# min: 가장 작은 값 반환
# max: 가장 큰 값 반환
print(min(1,2,3))
print(max([1,2,3]))

# eval: 문자열로 들어온 수식을 계산
print(eval("7+3"))

# sorted: iterable 객체 오름차순 정렬
# 정렬 기준은 key 속성을 이용해 명시
l = [3,5,2]
print(sorted(l))
print(sorted(l, reverse=True))

r = [("D", 4),("B",2),("A",1),("C",3)]
print(sorted(r, key = lambda x: x[1], reverse=False))