from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(m)]
w, b = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, team):
    queue = deque()
    queue.append((x,y))
    count = 1
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == team:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count

for i in range(m):
    for j in range(n):
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                w += dfs(i, j, graph[i][j]) ** 2
            else:
                b += dfs(i, j, graph[i][j]) ** 2

print(w, b)