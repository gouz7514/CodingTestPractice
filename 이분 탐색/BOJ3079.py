# 입국 심사
# 문제 링크 : https://www.acmicpc.net/problem/3079
# 문제 이해 : 3분
# 문제 해결 : low, high는 알겠는데 다음을 모르겠네..
# 왜 이렇게 어렵게 생각했지?
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

low, high = 0, max(arr) * m
answer = 0

while low <= high:
    mid = (low + high) // 2
    # mid 시간 안에 통과할 수 있는지 확인
    passed = 0
    for i in arr:
        passed += mid // i

    if passed < m:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1
print(answer)