# TODO : https://velog.io/@jwisgenius/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9

import time

start_time = int(round(time.time() * 1000))
arr = [i for i in range(1, 5)]
########################
# 1번 재귀 : 20824ms
# def permute(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result
#
# print(permute(arr))
##########
# 2번 itertools.permutations : 12258ms
# from itertools import permutations
#
# print(list(permutations(arr)))
#####################
# 3번 : 58535ms
def perm(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                result.append([lst[i]] + p)

    return result

print(perm(arr, 2))
################
# def perm(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
#     for i,elem in enumerate(arr):
#         for p in perm(arr[:i]+arr[i+1:], n-1):
#             result += [[elem] + p]
#     return result
# print(perm(arr, 5))
################
# def perm(arr, r, tmp, ans, used):
#     if len(tmp) == r:
#         print("tmp : ", tmp)
#         ans.append(tmp)
#         print("ans : ", ans)
#         return ans
#
#     for i in range(len(arr)):
#         if i in used:
#             continue
#         used.add(i)
#         tmp.append(arr[i])
#         perm(arr, r, tmp, ans, used)
#         tmp.pop()
#         used.remove(i)
#     return ans
# used = set()
# print(perm(arr, 4, [], [], used))
################
# def permutation(arr, r):
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]
#     return_array = []
#
#     def generate(chosen, used):
#         # 내가 원하는 만큼 뽑았으면, return
#         if len(chosen) == r:
#             return_array.append(''.join(chosen))
#             return
#
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#
#     generate([], used)
#     return return_array
################
# def perm(arr, depth, length, end):
#     if depth == end:
#         print(arr[:end])
#         return
#     for i in range(depth, length):
#         arr[i], arr[depth] = arr[depth], arr[i]
#         perm(arr, depth + 1, length, end)
#         arr[i], arr[depth] = arr[depth], arr[i]
#
# perm([1,2,3,4], 0, 4, 3)
################
end_time = int(round(time.time() * 1000))
print('실행 시간 : %d(ms)' % (end_time - start_time))
