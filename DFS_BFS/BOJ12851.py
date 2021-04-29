# 숨바꼭질 2
# 문제 링크 : https://www.acmicpc.net/problem/12851
# bfs는 확실한데...
# 아니 dfs인가? 레벨을 기억해야 하니까?
# 근데 dfs라면 제약이 있어야 하는데 이건 제약이 없다.. 커졌다가 작아졌다가 하니까
# dp까지 적용된 문제였네
from collections import deque

n, k = map(int, input().split())
ch = [[-1,0] for _ in range(100001)]  # [시간, 방법 수]

def bfs(n):
    queue = deque()
    queue.append(n)
    ch[n][0] = 0
    ch[n][1] = 1

    while queue:
        x = queue.popleft()
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001:
                if ch[i][0] == -1: # 처음 방문하는 경우
                    ch[i][0] = ch[x][0] + 1
                    ch[i][1] = ch[x][1]
                    queue.append(i)
                elif ch[i][0] == ch[x][0] + 1: # 한번 이상 방문한 경우
                    ch[i][1] += ch[x][1]

bfs(n)
print(ch[k][0])
print(ch[k][1])