# 단지 번호 붙이기
# 문제 링크 : https://www.acmicpc.net/problem/2667
n = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
arr = [list(map(int, list(input()))) for _ in range(n)]
answer = []

def dfs(x, y, cnt): # 세로, 가로, cnt
    arr[x][y] = 0 # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if arr[nx][ny] == 1:
            cnt = dfs(nx, ny, cnt+1)
    return cnt

for i in range(n): # 세로
    for j in range(n): # 가로
        if arr[i][j] == 1:
            answer.append(dfs(i, j, 1))

for i in sorted(answer):
    print(i)