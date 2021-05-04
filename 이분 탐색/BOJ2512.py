# 예산
# 문제 링크 : https://www.acmicpc.net/problem/2512
# 문제 이해 : 1분 30초
# 문제 해결 : 4분 20초
n = int(input())
budget = list(map(int, input().split()))
total = int(input())

budget.sort()
low, high = 0, budget[-1]
answer = 0

while low <= high:
    cur = 0
    mid = (low + high) // 2
    for b in budget:
        if b >= mid:
            cur += mid
        else:
            cur += b
    if cur <= total:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)