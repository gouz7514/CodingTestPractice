# 나이트의 이동
# 문제 링크 : https://www.acmicpc.net/problem/7562
# 문제 이해 : 1분 20초
# 문제 해결 : 25분
# 나이트는 총 8방향으로 이동 가능하다
# 최소 이동 횟수 구해야하니까 bfs로 가면서 cnt 동시에 세야겠네
# 풀이는 분명 맞는데 시간초과
# 방문 여부와 이동 횟수 동시에 처리하면 시간초과나네
# 아 어쨌든 도달하기만 하면 되니까 굳이 비교할 필요가 없구나
import sys
from collections import deque

dx = [2,2,1,1,-1,-1,-2,-2]
dy = [1,-1,2,-2,2,-2,1,-1]

def bfs(i, j, wx, wy):
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 1 # 방문처리
    while queue:
        x, y = queue.popleft()
        if x == wx and y == wy:
            print(arr[wx][wy] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if arr[nx][ny] == 0: # 처음 방문하는 경우
                arr[nx][ny] = 1 # 방문처리
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
            # else: # 한번 이상 방문한 경우 # 굳이 필요없는 과정
            #     arr[nx][ny] = min(arr[nx][ny], arr[x][y]+1)


for _ in range(int(sys.stdin.readline())):
    l = int(sys.stdin.readline()) # 체스판 한 변 길이
    arr = [[0 for _ in range(l)] for _ in range(l)] # 방문 여부, 이동 횟수
    cx, cy = map(int, sys.stdin.readline().split()) # 현재 있는 칸
    wx, wy = map(int, sys.stdin.readline().split()) # 이동하려는 칸
    bfs(cx, cy, wx, wy)