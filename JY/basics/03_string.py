# 문자열 자료형

# (1) 문자열 초기화
'''
- 큰 따옴표 구성 -> (내부) 작은 따옴표 사용 가능 
- 작은 따옴표 구성 -> (내부) 큰 따옴표 사용 가능
- 백슬래쉬 (\) 사용
'''
data = "Don't you know \"Python\"?"
print(data)


# (2) 문자열 연산
a = "Hello"
b = "Python!"
print(a+" "+b)

c = "String"
print(c*3)

'''
- 파이썬의 문자열은 내부적으로 리스트와 같이 처리 => 인덱싱과 슬라이싱 가능
'''
d = "ABCDE"
print(d[1:2])
