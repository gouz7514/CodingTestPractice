# 신입 사원
# 문제 링크 : https://www.acmicpc.net/problem/1946
# 문제 이해 : 40초
# 문제 해결 : 15분
# 전에 풀었던 문제인데도 이렇게 헷갈려버리네..
import sys

for _ in range(int(sys.stdin.readline())):
    N = int(input())
    candidate = []
    ans = N
    for _ in range(N):
        candidate.append(list(map(int, sys.stdin.readline().split())))

    candidate.sort()
    x = candidate[0][1]
    for i in range(1, N):
        if candidate[i][1] < x:
            x = candidate[i][1]
        else:
            ans -= 1
    print(ans)