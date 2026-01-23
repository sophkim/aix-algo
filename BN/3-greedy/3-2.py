# 3-2. 큰 수의 법칙

def large_num(n, m, k, arr):

    sorted_arr = sorted(arr, reverse=True)
    max1 = sorted_arr[0]
    max2 = sorted_arr[1]

    answer = 0

    for i in range(m):
        print("i: ", i, " answer: ", answer)

        if i == 0:
            answer += max1
        elif i % k != 0:
            answer += max1
        else:
            answer += max2
    return answer


answer = large_num(5, 8, 3, [2,4,5,4,6])
print(answer)
