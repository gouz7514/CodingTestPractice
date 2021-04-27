# 유기농 배추
# 문제 링크 : https://www.acmicpc.net/problem/1012
# 문제 이해 :
# 문제 해결 :
# 백준은 recursionlimit을 줘야 하네.
# 그렇다면 dfs가 아니라 bfs로도 풀어봐야겠다
import sys
sys.setrecursionlimit(3000000)

for _ in range(int(input())):
    m, n, k = map(int, input().split()) # 가로, 세로, 위치
    graph = [[0] * m for _ in range(n)]
    print("graph : ", graph)
    answer = 0

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n): # 세로
        for j in range(m): # 가로
            if dfs(i, j):
                answer += 1

    print(answer)