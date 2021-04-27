# 음식물 피하기
# 문제 링크 : https://www.acmicpc.net/problem/1743
# 문제 이해 : 1분
# 문제 해결 :
import sys
sys.setrecursionlimit(3000000)

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

def dfs(x, y, cnt):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt+1)
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res = dfs(i, j, 1)
            if res > answer:
                answer = res

print(answer)