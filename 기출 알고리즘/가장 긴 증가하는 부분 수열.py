# BOJ11053
# 문제 링크 : https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# 와 이거 굉장히 좋은 문제다!
# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
       if arr[i] > arr[j]: # 추가될 수 있는 증가부분수열 중
           dp[i] = max(dp[i], dp[j] + 1) # 가장 긴 수열의 길이에 1을 더한 값
print(max(dp))