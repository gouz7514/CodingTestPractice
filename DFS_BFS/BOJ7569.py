# 토마토
# 문제 링크 : https://www.acmicpc.net/problem/7569
# 문제 이해 : 2분
# 문제 해결 : 25분
# 시간 초과라니...
# 7576이랑 똑같이 풀면 되는구나. 변수 다시 잡고 sys.stdin.readline() 써서 해결함
from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split()) # 가로, 세로, 높이
arr = []
dw = [1,-1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
queue = deque()

for _ in range(h):
    arr.append([list(map(int, sys.stdin.readline().split())) for _ in range(n)])

for i in range(h): # 높이
    for j in range(n): # 세로
        for k in range(m): # 가로
            if arr[i][j][k] == 1:
                queue.append([i,j,k])

while queue:
    w, x, y = queue.popleft()
    for k in range(6):
        nw = w + dw[k]
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nw < h and 0 <= nx < n and 0 <= ny < m and arr[nw][nx][ny] == 0:
            arr[nw][nx][ny] = arr[w][x][y] + 1
            queue.append([nw, nx, ny])

result = -2
check = False # 안 익은게 있는지 체크

for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                check = True # 안 익은게 존재함
            result = max(result, k)

if check:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)