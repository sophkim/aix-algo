# sys 라이브러리 readline() 사용법

import sys

input_data = sys.stdin.readline().rstrip() # 문자열 마지막 공백 문자 제거를 위하여 rstrip() 사용

print(input_data)