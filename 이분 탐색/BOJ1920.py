# 수 찾기
# 문제 링크 : https://www.acmicpc.net/problem/1920
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
target = list(map(int, input().split()))

for t in target:
    low = 0
    high = len(arr) - 1
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > t:
            high = mid - 1
        elif arr[mid] < t:
            low = mid + 1
        else:
            answer = 1
            break
    print(answer)