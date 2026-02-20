# 입력 데이터가 많은 경우 sys 라이브러리의 readline() 함수 이용

import sys

# 하느의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

# 입력받은 문자열 그대로 출력
print(input_data)