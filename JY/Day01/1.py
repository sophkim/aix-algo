n = 1260
count = 0 # 거슬러줘야 하는 동전 최소 개수

c_500 = n // 500
count += c_500
n = n % 500 

c_100 = n // 100
count += c_100
n = n % 100 

c_50 = n // 50
count += c_50
n = n % 50 

c_10 = n // 10
count += c_10
n = n % 10 

print(count)


# 예시 답안
'''
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin 
    n = n % coin 

print(count)
'''
