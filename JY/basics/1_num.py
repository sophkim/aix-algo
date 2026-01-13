# 수 자료형

# 1. 정수형 (양의 정수, 음의 정수, 0)

a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)


# 2. 실수형 (양의 실수, 음의 실수)
'''
- 소수부가 0이거나 정수부가 0인 경우, 앞의 0을 생략할 수 있다.
- 매우 크거나 작은 수를 표현할 때 지수 표기법을 사용할 수 있다.
예를 들어, 값이 10억 미만이라고 가정하는 상황에서는 1e9와 같이 표현할 수 있다.
이러한 방식은 실수를 줄이는 데 도움이 된다.
- 실수형은 IEEE 754 표준을 기반으로 표현되므로, 정밀도에 한계가 존재한다.
- 정밀도 문제를 완화하기 위해 round() 함수를 사용할 수 있다: round(실수 데이터, 반올림하고자 하는 위치 - 1)
'''

b = 157.93
print(b)

b = -1837.2
print(b)

b = 5.
print(b)

b = -.8
print(b)


c = 1e9
print(c)

c = 75.25e1
print(c)

c = 3954e-3
print(c)


d = 0.3 + 0.6
print(d)

if d == 0.9:
    print(True)
else:
    print(False)


e = 0.3 + 0.6
e = round(e, 4)
print(e)

if e == 0.9:
    print(True)
else:
    print(False)
