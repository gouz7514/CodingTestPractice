import sys
sys.setrecursionlimit(300000)

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    u,v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)