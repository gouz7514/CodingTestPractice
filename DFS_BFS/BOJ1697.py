# 숨바꼭질
# 문제 링크 : https://www.acmicpc.net/problem/1697
from collections import deque

N, K =  map(int, input().split())
visited = [False] * 100001

def bfs(v):
    time = 0
    queue = deque([[v,time]])

    while queue:
        print("queue : ", queue)
        v = queue.popleft()
        e = v[0]
        count = v[1]
        if not visited[e]:
            visited[e] = True
            if e == K:
                return count
            count += 1
            if (e * 2) <= 100000:
                queue.append([e * 2, count])
            if (e + 1) <= 100000:
                queue.append([e + 1, count])
            if (e - 1) >= 0:
                queue.append([e - 1, count])
    return count
print(bfs(N))

# from collections import deque
#
# def bfs(v):
#     count = 0
#     q = deque([[v, count]])
#     while q:
#         v = q.popleft()
#         e = v[0]
#         count = v[1]
#         if not visited[e]:
#             visited[e] = True
#             if e == K:
#                 return count
#             count += 1
#             if (e * 2) <= 100000:
#                 q.append([e * 2, count])
#             if (e + 1) <= 100000:
#                 q.append([e + 1, count])
#             if (e - 1) >= 0:
#                 q.append([e - 1, count])
#     return count
#
#
# N, K = map(int, input().split())

# print(bfs(N))