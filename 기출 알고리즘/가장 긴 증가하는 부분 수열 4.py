n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]
array = [[x] for x in lst] # [[10], [20], [10], [30], [20], [50]]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]: # 증가하는 수열인데
            if dp[j] + 1 > dp[i]: # 이전꺼랑 연결할 수 있는 경우?
                array[i] = array[j] + [lst[i]]
                dp[i] = dp[j] + 1

length = 0
flag = 0

for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]

print(length)
print(*array[flag])