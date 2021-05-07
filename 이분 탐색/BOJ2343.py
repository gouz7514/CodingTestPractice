# 기타 레슨
# 문제 링크 : https://www.acmicpc.net/problem/2343
# 문제 이해 : 2분
# 문제 해결 : 아 이건 모르겠다
# 참고 링크 : https://jjangsungwon.tistory.com/49
# low, high를 정하는 융통성이 더 필요한 거 같다.
n, m = map(int, input().split())
arr = list(map(int, input().split()))

lesson_total = sum(arr)
left, right = lesson_total // m, lesson_total
answer = right

while left <= right:
    mid = (left + right) // 2
    # mid가 기타 레슨의 최댓값보다 작은지 판단. 작다면 기타 레슨을 담을 수 없으므로 left = mid + 1
    if mid < max(arr):
        left = mid + 1
        continue

    # mid 값으로 기타 레슨을 m개 이하의 구역으로 나눌 수 있는지 판단
    count, temp = 0, 0
    for i in range(len(arr)):
        if arr[i] > mid:
            break
        elif temp + arr[i] <= mid:
            temp += arr[i]
        else:
            temp = arr[i]
            count += 1

    # 나눌 수 있다면 더 작은 값 판단하기 위해 right = mid - 1
    if count <= m - 1:
        right = mid - 1
        answer = min(answer, mid)
    else: # 나눌 수 없다면 더 큰 값 판단하기 위해 left = mid + 1
        left = mid + 1

print(answer)