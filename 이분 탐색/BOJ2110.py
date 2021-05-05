# 공유기 설치
# 문제 링크 : https://www.acmicpc.net/problem/2110
# 조금 까다로운 문제구만
# mid 이상만큼 떨어진 데는 설치하고 다음 탐색
n, c = map(int, input().split())
arr = []
answer = 0

for _ in range(n):
    arr.append(int(input()))
arr.sort()
low, high = 1, arr[-1] - arr[0]

while low <= high:
    mid = (low + high) // 2
    prev = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] - prev >= mid:
            cnt += 1
            prev = arr[i]
    if cnt >= c:
        low = mid + 1
        answer = max(answer, mid)
    else:
        high = mid - 1
print(answer)