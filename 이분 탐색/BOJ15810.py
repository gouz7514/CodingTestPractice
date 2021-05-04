# 풍선 공장
# 문제 링크 : https://www.acmicpc.net/problem/15810
# 문제 이해 : 3분
# 문제 해결 : 4분
n, m = map(int, input().split()) # 스태프 수, 풍선 수
arr = list(map(int, input().split()))

arr.sort()
low, high = 0, arr[-1] * m
answer = 0

while low <= high:
    mid = (low + high) // 2
    cnt = 0
    for a in arr:
        cnt += mid // a

    if cnt >= m:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
print(answer)