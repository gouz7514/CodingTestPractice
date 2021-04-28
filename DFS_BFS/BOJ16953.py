# A → B
# 문제 링크 : https://www.acmicpc.net/problem/16953
# 이렇게 풀면 시간초과 뜨네
# from collections import deque
#
# a, b = map(int, input().split())
#
# def bfs(a):
#     visited = []
#     queue = deque()
#     queue.append([a, 0])
#     visited.append(a)
#
#     while queue:
#         num, cnt = queue.popleft()
#
#         if num == b:
#             return cnt + 1
#         for n in (num * 2, int(str(num) + '1')):
#             if n <= b:
#                 if n not in visited:
#                     queue.append([n, cnt + 1])
#                     visited.append(n)
#     return -1
#
# print(bfs(a))

# 남의 풀이
# queue에 (a, 1)을 넣는다.
# popleft를 통해 뽑은 숫자에서 가능한 연산을 한다.
# 2를 곱했을 때 b보다 크다면 queue에 넣지 않는다.
# 1을 수의 가장 오른쪽에 추가했을 때 b보다 크면 queue에 넣지 않는다.
from collections import deque

a,b = map(int, input().split())
answer = -1
queue = deque([(a, 1)])

while queue:
    i, cnt = queue.popleft()
    if i == b:
        answer = cnt
        break
    if i * 2 <= b:
        queue.append((i*2, cnt+1))
    if int(str(i) + '1') <= b:
        queue.append((int(str(i) + '1'), cnt+1))

print(answer)