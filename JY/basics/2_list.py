# 리스트 자료형 


# (1) 리스트 만들기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9] # 리스트 인덱스는 0부터 시작
print(a)
print(a[4]) # 다섯 번째 데이터 출력

a = list() # 빈 리스트 선언 방법 (1)
print(a)

a = [] # 빈 리스트 선언 방법 (2)
print(a)

n = 10
a = [0]*n # 모든 값이 0이고, 크기가 N인 1차원 리스트 생성
print(a)


# (2) 리스트의 인덱싱과 슬라이싱
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b[-1]) # 제일 마지막 데이터 출력
print(b[-3]) # 뒤에서 3번째 데이터 출력

b[3] = 7 # 4번째 데이터 변경
print(b) 

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4]) # 2번째 ~ 4번째 데이터 슬라이싱 


# (3) 리스트 컴프리헨션
'''
- 리스트 초기화 방법 중 하나
- 대괄호 안에 조건문과 반복문을 넣는 방식
- 이차원 리스트 초기화에 유용
'''
c = [i for i in range(20) if i % 2 == 1]
print(c)

c = [i*i for i in range(1, 10)]
print(c)

n = 3 # n x m 크기의 리스트
m = 4 
c = [[0]*m for _ in range(n)]
print(c)


# (3) 리스트 관련 메서드

d = [1 ,4, 3]
print(d)

d.append(2) # 원소 삽입
print(d)

d.sort() # 오름차순 정렬
print(d)

d.sort(reverse=True) # 내림차순 정렬
print(d)

d.reverse() # 원소 순서 반전
print(d)

d.insert(2,3) # (삽입할 위치 인덱스, 값)
print(d)

print(d.count(3)) # 특정 값인 데이터 개수

d.remove(3) # 특정 값 한 개 삭제
print(d)

# 특정 값 여러개 삭제 방법
e = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in e if i not in remove_set]
print(result)