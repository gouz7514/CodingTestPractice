# 주유소
# 문제 링크 : https://www.acmicpc.net/problem/13305
# 문제 이해 : 3분
# 문제 해결 : 40분 초과
import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split())) # 도로의 길이
price = list(map(int, sys.stdin.readline().split())) # 리터당 가격
answer = 0

p = price[0]

for i in range(len(road)):
    if price[i] <= p:
        p = price[i]
    answer += p * road[i]
print(answer)