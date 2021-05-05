# 서버실
# 문제 링크 : https://www.acmicpc.net/problem/17245
# 문제 이해 : 2분 30초
# 문제 해결 : 22분 40초
# 나눗셈 범위 잘 해결했다
import math

n = int(input())
arr = []
max_com = 0 # 최대 높이
tot_com = 0 # 컴퓨터 전체 갯수
minute = 0

for _ in range(n):
    x = list(map(int, input().split()))
    for i in x:
        tot_com += i
        if i > max_com:
            max_com = i
    arr.append(x)

low, high = 0, max_com

while low <= high:
    com = 0 # 정상 작동 컴퓨터 갯수
    mid = (low + high) // 2
    # arr 순회하면서 정상 작동하는 컴퓨터 갯수 count
    for ar in arr:
        for a in ar:
            com += min(mid, a)
    # 정상 동작 컴퓨터 수가 전체 컴퓨터의 절반 이상이면
    if com >= math.ceil(tot_com / 2): # 이 부분이 문제였음
        minute = mid
        high = mid - 1
    else:
        low = mid + 1
print(minute)