# 숫자 카드 2
# 문제 링크 : https://www.acmicpc.net/problem/10816
n = int(input())
cards = list(map(int, input().split()))
cards.sort()
dic = {}
for c in cards:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

m = int(input())
nums = list(map(int, input().split()))
answer = []

for n in nums:
    low = 0
    high = len(cards) - 1
    cnt = 0
    found = False
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] > n:
            high = mid - 1
        elif cards[mid] < n:
            low = mid + 1
        else:
            found = True
            break
    if found:
        answer.append(dic[n])
    else:
        answer.append(0)

print(*answer)