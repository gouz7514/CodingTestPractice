# from itertools import permutations
#
# n, m = map(int, input().split())
# arr = [0 for i in range(n)]
# # perm = list(permutations(arr, m))
# #
# # for p in perm:
# #     print(*p)
#
# # https://blog.encrypted.gg/945
# used = [0 for i in range(len(arr) + 1)]
# def func(k):
#     # 길이가 m이면 출력
#     if k == m:
#         for i in range(m):
#             print(arr[i], end=' ')
#         print('')
#         return
#
#     for i in range(1, n+1):
#         if not used[i]:
#             arr[k] = i
#             used[i] = 1
#             func(k+1)
#             used[i] = 0
#     return
#
# func(0)
####
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000000)
#
# def main():
#     n, m = [int(_) for _ in input().split()]
#     ans = [' ' for _ in range(m)]
#     visited = [False for _ in range(n+1)]
#
#     go(0, n, m, ans, visited)
#
#
# def go(idx, n, m, ans, visited):
#     if idx == m:
#         print(' '.join(ans))
#         return
#
#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         ans[idx] = str(i)
#         visited[i] = True
#         go(idx+1, n, m, ans, visited)
#         visited[i] = False
#
#
# main()
############
def permutation():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1,N+1):
        if i in arr:
            continue
        arr.append(i)
        permutation()
        arr.pop()

N,M = map(int,input().split())
arr= []
permutation()