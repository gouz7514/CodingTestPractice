from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    return arr[N-1][M-1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
print(arr)