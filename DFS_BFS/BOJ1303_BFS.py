# 전쟁 - 전투
# 문제 링크 : https://www.acmicpc.net/problem/1303
# 문제 이해 : 1분
# 문제 해결 :
# 이렇게 변수를 기억하고 더해야하는 문제는 어떻게 풀어야할까?
# 구분이 필요하면 BFS?
from collections import deque

n,m = map(int, input().split()) # 가로, 세로
graph = [list(input().strip()) for _ in range(m)]
w,b=0,0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,team):
    queue = deque()
    queue.append((x,y))
    count = 1
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n: # 아 시발
                continue
            if graph[nx][ny] == team:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                count += 1
    return count

for i in range(m): # 세로
    for j in range(n): # 가로
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                w += bfs(i,j,graph[i][j])**2
            else:
                b += bfs(i,j,graph[i][j])**2
print(w,b)