# Longest Common Substring
# 중간에 떨어져 있으면 안된다.
# 얘도 DP구나
# 같으면 그냥 더함. 그리고 ans에 max 비교
x = [1,2,3,2,1]
y = [3,2,1,4,7]

ans = 0
dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])

print(dp)
print(ans)