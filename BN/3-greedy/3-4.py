# 3-3. 1이 될 때까지

n, k = map(int, input().split())

count = 0

while n != 1:
    if n % k == 0:
        n = n / k
        #print("1: ", n)
        count += 1
    else:
        n -= 1
        #print("2: ", n)
        count += 1

print(count)