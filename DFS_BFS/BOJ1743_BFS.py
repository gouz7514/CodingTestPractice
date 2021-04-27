from collections import deque

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 방문처리하고
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res = bfs(i, j)
            if res > answer:
                answer = res

print(answer)