# itertools 라이브러리


# 반복되는 데이터를 처리하는 기능을 포함한 라이브러리 
# permutations(순열): 순서 고려, 중복 안됨
# combinations(조합): 순서 고려 안함, 중복 안됨
# product(중복 순열): 순서 고려, 중복 허용
# combinations_with_replacement(중복 조합): 순서 고려 안함, 중복 허용

from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) 
print(result)


from itertools import combinations

result2 = list(combinations(data, 3))
print(result2)


from itertools import product

result3 = list(product(data, repeat=2)) # repeat 속성값 필요
print(result3)


from itertools import combinations_with_replacement
result4 = list(combinations_with_replacement(data, 2))
print(result4)