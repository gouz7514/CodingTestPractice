# LCS (Longest Common Subsequence : 최장 공통 부분 수열)
# 문제 링크 : https://www.acmicpc.net/problem/9251
# 설명 : https://twinw.tistory.com/126
# 떨어져 있어도 상관 없다
# a = input()
a = 'CAPCAK'
# b = input()
b = 'ACAYKP'
dp = [[0]*(len(b)+1)for _ in range(len(a)+1)]

for i in range(1, len(a) + 1):
    isChange = False
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp)
text = ''
lcsLen = dp[-1][-1]

# dp배열의 마지막 원소를 기준으로 체크하면서 각 행, 열에 유일한 경우만 더해준다.
for i in range(len(a), 0, -1):
    for j in range(len(b), 0, -1):
        if dp[i][j] == lcsLen:
            rowCheck = False
            for k in range(j-1, 0, -1):
                if dp[i][k] == lcsLen:
                    rowCheck = True
                    break
            colCheck = False
            for k in range(i-1, 0, -1):
                if dp[k][j] == lcsLen:
                    colCheck = True
                    break
            if not rowCheck and not colCheck and lcsLen > 0:
                text = a[i-1] + text
                print("a[i-1] : ", a[i-1])
                lcsLen -= 1
                break
print(text)