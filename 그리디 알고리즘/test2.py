from collections import deque

n, m = map(int, input().split()) # 가로, 세로
graph = [list(input().strip()) for _ in range(m)]
w, b = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, team):
    queue = deque()
    queue.append((x,y))
    count = 1
    graph[x][y] = 0 # 방문처리하고
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] == team:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return 1 if count == 0 else count

for i in range(m):
    for j in range(n):
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                w += bfs(i, j, graph[i][j])**2
            else:
                b += bfs(i, j, graph[i][j])**2
print(w, b)