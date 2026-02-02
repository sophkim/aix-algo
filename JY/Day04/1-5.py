array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted 소스 코드
result = sorted(array) # 별도의 정렬된 리스트 반환
print("---------<sorted>---------")
print("result:",result)
print("array:",array)

# sort 소스 코드
print()
print("----------<sort>----------")
array.sort() # 해당 리스트에 적용 / 결과를 저장할 별도의 리스트 필요 없음
print("array:",array)

# key를 활용할 경우
print()
print("--------<key 값 활용>--------")
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting) # key 값에 함수가 들어가고, 이는 정렬 기준이 됨.
print(result)

result2 = sorted(array, key = lambda data:data[1]) # lambda 사용하는 방법
print(result2)

array.sort(key = lambda data : data[1])
print(array)