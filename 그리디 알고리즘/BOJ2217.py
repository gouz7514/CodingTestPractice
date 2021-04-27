# 로프
# 문제 링크 : https://www.acmicpc.net/problem/2217
n = int(input())
rope = []
max_weight = 0

for i in range(n):
    rope.append(int(input()))
rope.sort()

for i in range(n):
    ith_max_weight = rope[i] * (n - i)
    if ith_max_weight > max_weight:
        max_weight = ith_max_weight

print(max_weight)