from itertools import combinations

import time

start_time = int(round(time.time() * 1000))
########################
arr = [i for i in range(1,5)]
##################
# 실행 시간 : 906ms
# itertools.combinations
# print(list(combinations(arr, 10)))

##################
# 실행 시간 : 1827ms
def comb(lst, n):
    ret = []
    if n > len(lst):
        return ret
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret
print(comb(arr, 2))
##################
# 실행 시간 : 2464ms
# def comb(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
#     for i in range(len(arr)):
#         elem = arr[i]
#         rest_arr = arr[i+1:]
#         for c in comb(rest_arr, n-1):
#             result.append([elem] + c)
#     return result
# print(comb(arr, 10))
##################
def combination(array, r):
    chosen = []
    if r > len(array):
        return chosen
    if r == 1:
        for i in array:
            chosen.append(i)
    elif r > 1:
        # r 개 만큼 빼주는 이유 (순서가 고려사항이 아니기 때문에, r개는 고려하지 않아도 앞서서 정해진다)
        for i in range(len(array) - r + 1):
            for temp in combination(array[i + 1:], r - 1):
                chosen.append([array[i], temp])
    return chosen

print(combination("ABCD", 2))
##################
end_time = int(round(time.time() * 1000))
print('실행 시간 : %d(ms)' % (end_time - start_time))
