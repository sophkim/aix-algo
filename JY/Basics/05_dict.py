# 딕셔너리 자료형

'''
- 키와 값의 쌍으로 구성된 자료형
- 딕셔너리는 내부적으로 해시 테이블을 이용하므로 O(1)의 시간 복잡도를 가짐
'''

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['복숭아'] = 'peach'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지고 있는 데이터 존재")

# 관련 함수
'''
- keys(): 키 데이터만 뽑아 리스트 생성
- values(): 값 데이터만 뽑아서 리스트 생성
'''
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
