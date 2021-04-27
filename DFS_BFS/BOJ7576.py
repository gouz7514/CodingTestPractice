# 토마토
# 문제 링크 : https://www.acmicpc.net/problem/7576
# 문제 이해 : 50초
# 문제 해결 : tlqkf
# dfs가 아니라 bfs로 풀어야할거같네
from collections import deque

M, N = map(int, input().split()) # 가로, 세로
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])
# 아 토마토 위치를 queue에 다 넣고 시작하는구나!
while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 안익은게 있다면, 익은 것으로 바꿔준다
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            queue.append([nx, ny])
print("arr : ", arr)

# -1이 존재하니까 -2로 비교
result = -2
check = False # 안 익은게 있는지 체크

for i in arr:
    for j in i:
        if j == 0:
            check = True # 안 익은게 존재함
        result = max(result, j)

if check: # 안 익은게 있으면
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)