# 미로 탐색
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[a][b] + 1
                queue.append((nx, ny))
    return arr[N-1][M-1]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(bfs(0,0))