# 연구소
# 문제 링크 : https://www.acmicpc.net/problem/14502
# 문제 이해 : 1분 30초
# 문제 해결 : 1시간. 오래걸렸지만 풀었다!
# 아니 이해가 안가네 왜 arr이 바뀜?????
# 얕은 복사 깊은 복사..
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split()) # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]
zero = [] # 0이 있는 위치 모두 저장
answer = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            zero.append([i, j])

zero_cnt = [i for i in range(len(zero))]

for comb in combinations(zero_cnt, 3): # 무작위로 3개 뽑아서 벽 세우고
    arr2 = copy.deepcopy(arr) # 여기가 포인트

    for c in comb:
        arr2[zero[c][0]][zero[c][1]] = 1

    # 바이러스 퍼트리기
    virus = deque()
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 2:
                virus.append((i, j))

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr2[nx][ny] == 0:
                    arr2[nx][ny] = 2
                    virus.append((nx, ny))

    safe = 0

    # 안전 영역 크기 구하기
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                safe += 1
    if safe > answer:
        answer = safe

print(answer)