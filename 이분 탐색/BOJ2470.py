# 두 용액
# 문제 링크 : https://www.acmicpc.net/problem/2470
# 문제 이해 :
# 문제 해결 : 음양 기준이구나.. 음수면 그 윗 범위 탐색, 양수면 그 아래 범위 탐색
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

low, high = 0, n - 1
diff = abs(arr[low] + arr[high])
answer = [arr[low], arr[high]]

while low < high:
    mid = arr[low] + arr[high]
    if abs(mid) < diff:
        answer = [arr[low], arr[high]]
        diff = abs(mid)
        if mid == 0:
            break
    if mid < 0:
        low += 1
    else:
        high -= 1
print(answer[0], answer[1])