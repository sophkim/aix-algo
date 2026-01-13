# collections 라이브러리


# deque: 인덱싱이나 슬라이싱 불가능. 그러나 제일 앞 데이터 접근을 효과적으로 수행 
'''
- popleft(): 첫 번째 요소 제거
- pop(): 마지막 원소 제거
- appendleft(x): x를 첫 번째 인덱스 위치에 삽입
- append(x): x를 가장 마지막 인덱스 위치에 삽입
'''

from collections import deque

data = deque([2,3,4])
data.append(5)
data.appendleft(1)

print(list(data))


# Counter
'''
- 등장 횟수 카운터
- iterable 객체가 주어지면, 해당 객체 내부의 원소가 몇 번씩 등장했는지 카운트
'''
from collections import Counter

cnt = ['r', 'b', 'r', 'g', 'b', 'b']
count = Counter(cnt)
print(count)
print(count['b'])
print(dict(count))
