# 나무 자르기
# 문제 링크 : https://www.acmicpc.net/problem/2805
# 문제 이해 : 1분 23초
# 문제 해결 : 1시간 걸리네 ㅋㅋ
# 아 시간초과 해결 못하겠다
# python이 아니라 pypy3?
import sys

n, m = map(int, sys.stdin.readline().split()) # 나무의 수, 가져가고자 하는 나무 길이
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()
result = 0
low, high = 0, trees[n-1]

while low <= high:
    answer = 0
    mid = (low + high) // 2
    for t in trees:
        if t > mid:
            answer += (t - mid)
    if answer >= m:
        low = mid + 1
        result = mid
    else:
        high = mid - 1

print(result)