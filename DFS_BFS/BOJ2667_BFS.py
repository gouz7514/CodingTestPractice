from collections import deque

n = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = [list(map(int, list(input()))) for _ in range(n)]
answer = []

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 0 # 방문처리
    cnt = 1 # 0으로 시작하면 한 채밖에 없는 집은 카운트되지 않는다
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))
for a in sorted(answer):
    print(a)