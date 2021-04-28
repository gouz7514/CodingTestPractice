# 영역 구하기
# 문제 링크 : https://www.acmicpc.net/problem/2583
# 문제 이해 : 3분
# 문제 해결 : 10분
# 와 퍼펙트하게 풀었다!
from collections import deque

m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
answer = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(k):
    loc = list(map(int, input().split()))
    lx, ly = loc[0], loc[1] # 왼쪽 아래 x,y 좌표
    rx, ry = loc[2], loc[3] # 오른쪽 위 x, y 좌표

    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    cnt = 1 # 하나 있는 구역 체크하기 위해서 1부터 시작
    arr[i][j] = 1 # 방문처리
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            answer.append(bfs(i, j))

print(len(answer))
for i in sorted(answer):
    print(i, end=' ')