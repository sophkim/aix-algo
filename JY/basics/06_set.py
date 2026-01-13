# 집합 자료형 

'''
- 중복을 허용하지 않음
- 순서가 없음 ()
'''

a = set([1,2,3])
print(a)

b = {2,3,4,5,6}
print(b)

# 연산 (합집합, 교집합, 차집합)
print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

# 관련 함수
'''
- add(): 새로운 값 (1개) 추가
- update(): 새로운 값 (여러개) 추가
- remove(): 특정 값 제거
'''
data = set([1,2,3])
data.add(4)
data.update([5,6])
data.remove(6)

print(data)
