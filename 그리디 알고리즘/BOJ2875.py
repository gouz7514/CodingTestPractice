# 대회 or 인턴
n, m, k = map(int, input().split())
# cnt = 0
# while n + m >= k and n >= 0 and m >= 0:
#     n -= 2
#     m -= 1
#     cnt += 1
# print(cnt - 1)

team = 0
while n+m-3 >= k and n >= 2 and m >= 1:
    team += 1
    n -= 2
    m -= 1
print(team)