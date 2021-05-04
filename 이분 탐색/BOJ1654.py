# 랜선 자르기
# 문제 링크 : https://www.acmicpc.net/problem/1654
# 문제 이해 : 3분 10초
# 문제 해결 : 19분
# ZeroDivisionError?
# 반례 잘 찾았다
k, n = map(int, input().split())
lines = [] # 이미 가지고 있는 랜선들
for _ in range(k):
    lines.append(int(input()))

lines.sort()
result = 0
low, high = 0, lines[k-1]

while low <= high:
    answer = 0
    mid = (low + high) // 2

    if mid == 0:
        result = 1
        break
    else:
        for l in lines:
            answer += l // mid
    if answer >= n:
        low = mid + 1
        result = mid
    else:
        high = mid - 1
print(result)