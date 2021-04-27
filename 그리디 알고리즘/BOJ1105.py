# 팔
# 문제 링크 : https://www.acmicpc.net/problem/1105
# 문제 이해 : 1분 10초
# 문제 해결 : 와 이건 아예 해결책이 생각나지 않는다
# 자릿수 다른 경우에는 무조건 0이다
# 첫자리 숫자가 다른 경우 역시 0
# 그 다음부터 각자리 숫자가 다른 경우는 이전까지 누적 횟수가 최소 횟수이다.
L, R = map(str, input().split())
ans = 0

if len(L) != len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                ans += 1
        else:
            break
    print(ans)