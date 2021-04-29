# 탈출
# 문제 링크 : https://www.acmicpc.net/problem/3055
# 문제 이해 : 2분 30초
# 문제 해결 : tlqkf
# 1. 물이 차 있을 예정인 곳은 이동하지 못하므로 물을 이동시키고 고슴도치를 이동시킨다
# 2. 반드시 물은 비버굴에 이동할 수 없다
# 3. 고슴도치가 비버굴에 도착하면 이동한 시간 출력
# 4. 큐가 비어도 비버굴에 도착하지 못하면 KAKTUS
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == '.' and c[nx][ny] == 0: # 고슴도치가 갈 수 있고 방문하지 않았으면
                        c[nx][ny] = c[x][y] + 1 # 방문 처리
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(c[x][y])
                        return
            qlen -= 1
        water()

    print("KAKTUS")
    return

def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == '.': # 물 흘려보낸다
                    a[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]
c = [[0]*m for _ in range(n)]
q, wq = deque(), deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S': # 고슴도치
            x1, y1 = i, j # 변수에 기억시키고
            a[i][j] = '.' # 물 흐를 수 있도록
        elif a[i][j] == '*': # 물
            wq.append([i, j])

water()
bfs(x1, y1)