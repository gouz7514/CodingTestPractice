# 1. 물이 차 있을 예정인 곳은 이동하지 못하므로 물을 이동시키고 고슴도치를 이동시킨다
# 2. 물은 반드시 비버굴에 이동할 수 없다.
# 3. 고슴도치가 비버굴에 도착하면 이동한 시간 출력
# 4. 큐가 비어도 비버굴에 도착하지 못하면 KAKTUS
# 일정 단계별로 반복하는 경우
# while queue 안에 queue의 길이를 변수로 받아서 하나씩 빼주는 기술 활용 가능
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

r, c = map(int, input().split())
arr = [list(map(str, input())) for _ in range(r)]
c = [[0] * r for _ in range(c)] # 방문 처리할 배열
q, wq = deque(), deque()

# 고슴도치 이동
def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1 # 방문처리 : 한번 간 곳 또 들르지 않도록
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == '.' and c[nx][ny] == 0: # 고슴도치가 갈 수 있고 방문하지 않았다면
                        c[nx][ny] = c[x][y] + 1
                        q.append([nx, ny])
                    elif arr[nx][ny] == 'D':
                        print(c[nx][ny])
                        return
            qlen -= 1
        water()

# 물 흐르도록
def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S': # 고슴도치
            x1, y1 = i, j # 변수에 기억시키고
            arr[i][j] = '.'
        elif arr[i][j] == '*': # 물
            wq.append([i, j])

water()
bfs(x1, y1)