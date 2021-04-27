# DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())
visit = [0 for _ in range(n+1)]
adj = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

def dfs(v):
    print(v, end=' ')
    visit[v] = True
    for i in range(1, n+1):
        if visit[i] == 0 and adj[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visit[v] = 1
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1, n+1):
            if visit[i] == 0 and adj[x][i] == 1:
                queue.append(i)
                visit[i] = 1

dfs(v)
visit = [0 for _ in range(n+1)]
print()
bfs(v)