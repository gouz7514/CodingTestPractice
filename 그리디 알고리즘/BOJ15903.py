# 카드 합체 놀이
# 문제 링크 : https://www.acmicpc.net/problem/15903
# 문제 이해 : 1분 30초
# 문제 해결 : 7분
# 최소 힙 이용할 수 있을 것 같다
# 적절한 자료구조 이용해서 잘 풀었다.
import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

while m != 0:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x + y)
    heapq.heappush(cards, x + y)
    m -= 1

print(sum(cards))