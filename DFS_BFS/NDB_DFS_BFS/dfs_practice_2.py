# Stack은 쌓고 나중에 쌓인 애 기준으로 출력된다
def dfs(graph, v, visited):
    # print(v, end=' ')
    stack = [v]
    while stack:
        s = stack.pop()
        visited[s] = True
        for i in graph[s]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
        print(s, end=' ')


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, 1, visited)