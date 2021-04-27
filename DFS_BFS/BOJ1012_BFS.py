from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    m, n, k = map(int, input().split()) # 가로, 세로, 위치
    graph = [[0] * m for _ in range(n)]
    answer = 0

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0 # 방문처리
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return True

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if bfs(i, j):
                    answer += 1

    print(answer)