# 이분 탐색 사용한다
n = int(input())
arr = list(map(int, input().split()))
stack = [0]

def find(target):
    l, h = 1, len(stack) - 1
    while l < h:
        m = (l + h) // 2
        if stack[m] < target:
            l = m + 1
        elif stack[m] > target:
            h = m
        else:
            l = h = m
    return h

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a

print(len(stack) - 1)

############
from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))