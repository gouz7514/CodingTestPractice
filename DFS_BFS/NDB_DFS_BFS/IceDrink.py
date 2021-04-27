"""
1. 특정 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서
아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
2. 방문한 지점에서 다시 상,하,좌,우를 살펴보면서 방문을 진행하는 과정을 반복하면,
연결된 모든 지점을 방문할 수 있습니다.
3. 모든 노드에 대해 1,2의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다.
"""
N, M = map(int, input().split())


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True  # 방문이 다 끝났으니까 True
    return False


graph = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
